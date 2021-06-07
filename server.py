
from flask import FLask

app = Flask(__name__)


@app.route('/')
def homepage():

    return "<html><body><h1>This is the homepage</h1></body></html>"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')