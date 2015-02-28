import system
sys.path.insert(0, '/Users/josephwon/Documents/donateMyo')

from flask import Flask
app = Flask(__name__)


@app.route("/")
def index():
	return "Dwonate"

if __name__ == "__main__":
	app.run()