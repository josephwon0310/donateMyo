import fetcher

from flask import Flask, request, render_template
from dwolla import transactions, constants
import request
app = Flask(__name__)


@app.route("/")
def index():
	return render_template('index.html')

@app.route('/donate')
def donate():
	#while(True):
		#request.get_total()

	return render_template('donate.html')


if __name__ == "__main__":
	app.run(debug=True)