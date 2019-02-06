# $ export FLASK_APP=hello.py
# $ python -m flask run

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
# def hello_world():
#     return 'Hello, World!'
