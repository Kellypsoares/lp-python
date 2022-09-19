from flask import Flask


pf = Flask(__name__)

@pf.route("/")

def hello_world():
    return "<p>Hello, World!</p>"
pf.run()
