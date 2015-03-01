import multiprocessing, subprocess, threading, time
import fetcher
import request
import myo_control
from flask import Flask, request, render_template
from dwolla import transactions, constants, accounts
app = Flask(__name__)

#Dwolla user config
constants.sandbox=True
constants.client_id = "+KTelCvoC8PFYUbH3kWYAwtSylM5GCD1h9NrgZDtGTu98HmJQu"
constants.client_secret = "aImQ1onBcklDmG2yqOXXb21GLWeqR7Cg7cLIAs9Woh6fR15D+h"
constants.access_token = "uUnrT/TEJoZDPoHb2YJh/4quuEKZOWjfXQ26a9n+4M8bO89Epb"
constants.pin = "0310"

f = open("pose.txt", "r")

def myo():
	myo_control.main()

writing = multiprocessing.Process(target=myo)

def reader():
    pose = subprocess.check_output(['tail', '-1', "pose.txt"])
    if "finger" in str(pose) or "wave_out" in str(pose):
    	print "YO!"
    threading.Timer(2,reader).start()

reading = multiprocessing.Process(target=reader)

@app.route("/")
def index():
	return render_template('index.html')

@app.route('/donate', methods=['POST'])
def donate():
	recipient = request.form['id']
	balance = accounts.balance()
	return render_template('donate.html', balance=balance)


if __name__ == "__main__":
	#reading.start()
	writing.start()
	app.run(debug=True)