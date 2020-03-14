from flask import Flask
app = Flask(__name__)

@app.route('/')
def default_page():
	return "from Bean service"

if __name__ == '__main__':
	app.run(host="0.0.0.0",port="4000", debug=True)

