from flask import Flask, request, render_template, url_for, redirect, flash
import json
from random import randint
import requests


app = Flask(__name__)

app.config.update(
    DEBUG = True,
    SECRET_KEY = 'foobar'
)

def load_json(filename):
    with open(filename, 'r') as f:
        content = f.read()
        return json.load(f)


@app.route("/random", methods=["POST"])
def random_dish():



if __name__ == '__main__':
    app.run()
