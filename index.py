# $ export FLASK_APP=hello.py
# $ python -m flask run

from flask import Flask, render_template
import tweetgen


f = open('./ive-random.txt' , 'r')
file = [word for line in f.read().split('\n') for word in line.split(' ')]
f.close()
# file = ['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish']

app = Flask(__name__)
@app.route('/')
def index():
    hist = tweetgen.histogram(file)
    text = tweetgen.sample_words_by_frequency(hist, 10)
    return render_template('index.html', text = text)
# def hello_world():
#     return 'Hello, World!'
# text = "Here's my first flask app!"
