from flask import Flask  # inside a module flask there  is a class named Flask so we will import this

app = Flask(
  __name__
)  #intializing the flask app, actually we are creating an object of the class Flask that we imported

print(__name__)


@app.route("/")
def hello_world():
  return "<p>Hello, World!</p>"


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)