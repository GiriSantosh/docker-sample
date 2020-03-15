from flask import Flask
app = Flask(__name__)

@app.route('/')
def default_page():
	return "from REPORT service"

if __name__ == '__main__':
	app.run(host="0.0.0.0", debug=True)

