# Sentiment Web App
This is a simple web app that takes in text input(sentiment)
and processes it to produce the probability of the sentiment
being positive. It's a beginner to intermediate level project that can help 
you get started with Natural Language processing.This was my end of class project 
It's built using flask and python and currently 
hosted on heroku at 
[invitech-sentiment-app](https://invitech-sentiment-app.herokuapp.com/index). 
It's hosted version is only having a 76% accuracy because I used a less complex model due to the free RAM space provided by heroku.
However the notebook has a better model that you can uncomment and run with a far better accuracy.
## Table of Contents
* [Technologies](#technologies)
* [Features](#features)
* [Setup](#setup)
* [Other information](#other-information) 
* [License](#license)
### Technologies
* [dill 0.3.3](https://pypi.org/project/dill/)
* [flask 1.1.2](https://pypi.org/project/Flask/)
* [scikit-learn 0.23.2](https://scikit-learn.org/stable/whats_new/v0.23.html)
* [spacy 2.3.2](https://pypi.org/project/spacy/)
* [pandas 1.1.1](https://pandas.pydata.org/pandas-docs/version/1.1.1/user_guide/index.html)
* [gzip 3.9.1](https://docs.python.org/3/library/gzip.html)
### Features
* Write text in a textbox 
* Submit for predicting using submit button
* Access the predict method through url like an API
### Setup

Make sure you [clone](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository) the source code on your local machine.
Below is a code example showing how to access the predict method through the url on your local machine,
you can also replace the url with ``url = "https://invitech-sentiment-app.herokuapp.com/"`` if you prefer accessing the hosted url
```
import requests
url = "http://127.0.0.1:5000/"    # url should be the one of your local machine which appears when you run the program
tweet = "I like this program, it runs well on my machine!"    # You can put in your own text
response = requests.get(url+"predict",params ={"tweet":tweet})
response.text

``` 
   
* The model was built using [Anaconda](https://docs.anaconda.com/anaconda/install/) jupyter notebook 
* App built using [pycharm](https://www.jetbrains.com/pycharm/) editor
### Other information
How to deploy apps on [heroku](https://devcenter.heroku.com/start)
### License
This project is licensed under [MIT license](./LICENSE) terms
