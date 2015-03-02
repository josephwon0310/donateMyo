import multiprocessing, subprocess, threading, time, os, signal
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

result = []

def myo_run():
	myo_control.main()

myo = multiprocessing.Process(target=myo_run)

def reader():
    pose = subprocess.check_output(['tail', '-1', "pose.txt"])
    money = 0
    if "finger" in str(pose) or "wave_out" in str(pose):
    	result.append(1)

    if "fist" in str(pose):
    	time.sleep(1)
    	myo.terminate()
    	for send in result:
    		money += 5

    	print(transactions.send('812-197-4121',money))
    	print "Transaction Complete!"
    	time.sleep(30)

    t = threading.Timer(0.5, reader).start()



@app.route("/")
def index():
	return render_template('index.html')

@app.route('/donate', methods=['POST'])
def donate():
	reader()
	myo.start()
	balance = accounts.balance()
	return render_template('donate.html', balance=balance)


if __name__ == "__main__":
	app.run(debug=True)









