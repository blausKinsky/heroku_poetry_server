from flask import Flask, render_template
import random

# app = Flask(__name__)

greets = ["Hello", "Hi", "Salutations", "Greetings", "Hey", "Sup"]
places = ["region", "continent", "world", "solar system",
  "galaxy"]

# @app.route('/hello')
def hello():
  greeting = random.choice(greets) + ", " + random.choice(places)
  return render_template("greetings.html",
    greet=random.choice(greets), place=random.choice(places))

# if __name__ == '__main__':
#   app.run()

def gen_random():
  n = random.random()
  return n

#to run this code, cd into the location where the file is and then goto your browser: localhost:5000/hello