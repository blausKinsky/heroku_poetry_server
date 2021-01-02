from flask import Flask, render_template, request, jsonify
import random
import sys
import nltk
import time
# import fp

app = Flask(__name__)



@app.route('/')
def welcome():
    return(render_template('index.html'))

@app.route('/api/', methods=["GET"])
def main_interface():
    #This is where we'd want to put our text-generating code
    print('getting a request')
    return jsonify('we have text now' * random.randrange(1, 10))

@app.after_request
def add_headers(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    return response


if __name__ == '__main__':
  app.run(debug=True)




