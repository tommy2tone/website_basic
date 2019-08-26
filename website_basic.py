# Basic website using Flask framework
# View on localhost:5000

from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return "Homepage content goes here"


@app.route('/about/')
def about():
    return "About content goes here"


if __name__ == "__main__":
    app.run(debug=True)