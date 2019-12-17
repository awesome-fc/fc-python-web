# coding=utf-8
import sys
import os

try:
    from urllib.parse import urlparse, urlencode
except ImportError:
    from urlparse import urlparse

# load local django
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "HelloWorld"))

import django

print (django.__version__)

base_path = None

from HelloWorld.wsgi import application

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

	return application(environ, start_response)
