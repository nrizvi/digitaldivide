# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 13:48:49 2020

@author: NabaDev
"""

import os
from flask import Flask, Blueprint, render_template, request, make_response, json, jsonify, current_app, abort, redirect
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
import json

# Your Account SID from twilio.com/console
account_sid = "ACd5b292430364bdc60dbbe67c83794dd9"
# Your Auth Token from twilio.com/console
auth_token  = "309bf64bcb1a1bdbc87535e4e8e33f47"
client = Client(account_sid, auth_token)

app = Blueprint('app', __name__)

@app.route('/')
def view():
    requests_file = os.path.join(current_app.static_folder, 'requests.json')
    with open (requests_file) as file:
        data = json.load(file)
        test_dict = {"req_id": 99,
		"name": "Fergilicious",
		"mobile": "(858) 123-9999",
		"device_type": "laptop",
		"zipcode": 92001,
		"wifi_enabled": True,
		"ram": 8,
		"storage": 512}
        data['requests'].append(test_dict)
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
    # get the form from http POST request
    requester_name = request.form['name']
    phone_number = request.form['mobile']
    zipcode = request.form['zipcode']
    print(request.form)
    test_dict = {'test1':'works'}
    #data_dict = {'name': requester_name, 'mobile': phone_number, 'zipcode':zipcode}
    return 'JSON posted'


@app.route("/getjson", methods=["GET"])
def starting_url():
    json_data = request.json
    a_value = json_data["a_key"]
    return "JSON value sent: " + a_value

# @app.route('/webhook', methods=['POST'])
# def webhook():
#     if request.method == 'POST':
#         """Send a dynamic reply to an incoming text message"""
#         # Get the message the user sent our Twilio number
#         # body = request.values.get('Body', None)
#         from_zip = request.values.get('FromZip', None)
#         print(from_zip)
#         response = MessagingResponse()
#         response.message('This is message 1 of 2.')
#         response.message('This is message 2 of 2.')

#         # msg.media("https://farm8.staticflickr.com/7090/6941316406_80b4d6d50e_z_d.jpg")

#         # Determine the right reply for this message
        

#         return str(response), 200

#     else:
#         abort(400)

# end sample code


if __name__ == '__main__':
    flask = Flask(__name__)
    flask.register_blueprint(app, url_prefix='/')

    flask.run()