# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 13:48:49 2020

@author: NabaDev
"""


from flask import Flask, Blueprint

hello = Blueprint('hello', __name__)

@hello.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app = Flask(__name__)
    app.register_blueprint(hello, url_prefix='/')

    app.run()