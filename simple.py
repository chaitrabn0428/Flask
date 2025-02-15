from flask import Flask

app = Flask(__name__)

@app.route('/')
def helloworld():
    return "<h1> hi all</h1>"

@app.route('/greet')
def index():
    return "<h1> hi how are you</h1>"