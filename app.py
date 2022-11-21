from flask import Flask, render_template, Response
from flask_cors import cross_origin
from urllib.request import urlopen

app = Flask(__name__)

@app.route('/test')
def hello():
    with urlopen('http://127.0.0.1:10707//vinorsoft/streamingcamera/v1.0/processManagement/get-path-streaming/?camera_id=cam1&height_resolution=234&width_resolution=416/') as r:
        text = r.read()
    return text

@app.route('/', methods=["GET"])
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
