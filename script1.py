from flask import Flask, render_template, Markup
import random
from datetime import time
import pygal

values = [0,12,13,14]
num = 0

app = Flask(__name__)
@app.route('/')


def home():
    i = 1
    while i < 6:
        bass = random.randint(1, 190)
        bas = bass - 1
        return render_template("home.html", output=bass, out=bas)



if __name__ == "__main__":
    app.run(host='0.0.0.0',port='00',debug=True)