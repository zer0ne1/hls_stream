from flask import Flask, render_template, Response
from flask_cors import cross_origin
from urllib.request import urlopen

app = Flask(__name__)

@app.route('/', methods=["GET"])
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
