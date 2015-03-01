import multiprocessing, subprocess
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

f = open('pose.txt', 'r')

def myo():
	myo_control.main()


@app.route("/")
def index():
	return render_template('index.html')

@app.route('/donate', methods=['POST'])
def donate():
	recipient = request.form['id']
	balance = accounts.balance()
	return render_template('donate.html', balance=balance)

#@app.route('/donate/<rain>')
#def rain():


if __name__ == "__main__":
	writing = multiprocessing.Process(target=myo)
	writing.start()
	app.run(debug=True)