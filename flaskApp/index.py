#!/usr/bin/env python
# coding=utf-8
from flask import Flask
from flask import request
from flask import make_response

try:
    from urllib.parse import urlparse, urlencode
except ImportError:
    from urlparse import urlparse

app = Flask(__name__)

base_path = ''

@app.route('/', methods=['GET', 'POST'])
def home():
    resp = make_response('<h1>Home Flask<h1>', 200)
    return resp

@app.route('/signin', methods=['GET'])
def signin_form():
    html = '''<form action="/signin" method="post">
         <p><input name="username"></p>
         <p><input name="password" type="password"></p>
         <p><button type="submit">Sign In</button></p>
         </form>'''

    resp = make_response(html, 200)
    return resp

@app.route('/signin', methods=['POST'])
def signin():
    if request.form['username']=='admin' and request.form['password']=='password':
        html = '<h3>Hello, admin!</h3>'
    else:
        html = '<h3>Bad username or password.</h3>'
    resp = make_response(html, 200)
    return resp

def handler(environ, start_response):
	# 如果没有使用自定义域名
    if environ['fc.request_uri'].startswith("/2016-08-15/proxy"):
        parsed_tuple = urlparse(environ['fc.request_uri'])
        li = parsed_tuple.path.split('/')
        global base_path
        if not base_path:
            base_path = "/".join(li[0:5])

        context = environ['fc.context']
        environ['HTTP_HOST'] = '{}.{}.fc.aliyuncs.com'.format(context.account_id, context.region)
        environ['SCRIPT_NAME'] = base_path + '/'

    return app(environ, start_response)

