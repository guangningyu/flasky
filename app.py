#!/usr/bin/env python

import os
from flask import Flask
# There are two contexts in Flask: the application context and the request context.
from flask import request
from flask import make_response
from flask import redirect
from flask import abort
from flask import render_template

# Flask uses the __name__ argument to determine the root path of the application so that
# it later can find resource files relative to the location of the application.
app = Flask(__name__)

@app.route('/')
def index():
    #return '<h1>Hello World!</h1>'
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    #return '<h1>Hello, %s!</h1>' % name
    return render_template('user.html', name=name)

@app.route('/browser')
def get_browser():
    user_agent = request.headers.get('User-Agent')
    return '<h1>Your browser is %s</h1>' % user_agent

@app.route('/set_cookie')
def set_cookie():
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer', '42')
    return response

@app.route('/redirect')
def test_redirect():
    return redirect('http://www.bing.com')

@app.route('/abort')
def test_abort():
    abort(404)
    return '<h1>You should not see this.</h1>'


if __name__ == '__main__':
    host = os.environ.get('HOST', '0.0.0.0')
    port = os.environ.get('PORT', '5000')
    app.run(host=host, port=int(port), debug=True)

