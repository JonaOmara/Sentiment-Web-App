#! /usr/bin/python3
from flask import Flask, request, render_template, redirect
import gzip
import dill

app = Flask(__name__)


@app.route("/")
def main():
    return redirect("/index")


@app.route('/index', methods=['GET'])
def index():
    return render_template('/index.html')


@app.route('/about')
def about():
    return 'This is about Sentiment Analysis'


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'GET':
        tweet = request.args.get('tweet')
    else:
        tweet = request.form['text']

    with gzip.open('SentimentModel.dill.gz', 'rb') as f:
        model = dill.load(f)
    probability = model.predict_proba([tweet])[0, 1]
    return 'Positive sentiment {}'.format(probability)


if __name__ == '__main__':
    app.run()
