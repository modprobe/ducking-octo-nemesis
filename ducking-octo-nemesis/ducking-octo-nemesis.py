from flask import Flask, request, render_template, url_for
from random import randint
import requests


app = Flask(__name__)

app.config.update(
    DEBUG=True,
    SECRET_KEY='foobar'
)


def load(filename):
    with open(filename, 'r') as f:
        return f.read().split('\n')


def random_dish():
    f = load("static/menu.txt")
    r = randint(0, len(f)-1)
    return f[r]


@app.route("/", methods=["GET", "POST"])
def generate_random():
    if request.method == "POST":
        return render_template('base.html', result=random_dish())
    else:
        return render_template('base.html')

if __name__ == '__main__':
    app.run()
