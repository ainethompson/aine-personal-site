
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def homepage():

    return render_template("homepage.html")


@app.route('/resume')
def show_resume():
    pass


@app.route('/about-me')
def show_bio():
    """ Show my personal bio, passions, etc. """
    return render_template("bio.html")


@app.route('/my-background')
def show_my_background():
    """ Show page with info about my education/coding background """

    return render_template("my-background.html")



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


# use 0.0.0.0:5000 in browser, not http://10.0.2.15:5000/