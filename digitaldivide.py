# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 13:48:49 2020

@author: NabaDev
"""

import os
from flask import Flask, Blueprint, render_template, request, make_response, json, jsonify, current_app

app = Blueprint('app', __name__)

@app.route('/')
def view():
    requests_file = os.path.join(current_app.static_folder, 'requests.json')
    with open (requests_file) as file:
        data = json.load(file)
    return render_template('view.html', data=data)

@app.route('/donate')
def donate():
    return render_template('form.html')
    #return 'Hello, World!'

# below are sample code, not actually used
@app.route('/postjson', methods = ['POST'])
def postJsonHandler():
    print (request.is_json)
    content = request.get_json()
    print (content)
    return 'JSON posted'

@app.route("/getjson", methods=["GET"])
def starting_url():
    json_data = request.json
    a_value = json_data["a_key"]
    return "JSON value sent: " + a_value
# end sample code

if __name__ == '__main__':
    flask = Flask(__name__)
    flask.register_blueprint(app, url_prefix='/')

    flask.run()