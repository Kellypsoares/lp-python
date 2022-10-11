from flask import Flask, render_template
from control import vcard 
app = Flask(__name__)

@app.route