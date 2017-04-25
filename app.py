#!/usr/bin/env python

import os
from flask import Flask

# Flask uses the __name__ argument to determine the root path of the application so that
# it later can find resource files relative to the location of the application.
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World</h1>'

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!</h1>' % name

if __name__ == '__main__':
    host = os.environ.get('HOST', '0.0.0.0')
    port = os.environ.get('PORT', '5000')
    app.run(host=host, port=int(port), debug=True)

