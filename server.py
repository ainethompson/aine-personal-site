
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def homepage():

    return render_template("homepage.html")
    # "<html><body><h1>This is the homepage</h1></body></html>"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')