from flask import Flask, escape, request,render_template

app = Flask(__name__)

@app.route('/')
def hello():
    render_template('intro.html')
