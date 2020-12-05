# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 13:48:49 2020

@author: NabaDev
"""

import os
from flask import Flask, Blueprint, render_template, request, make_response, json, jsonify, current_app, abort, redirect
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client

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

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        # print(request.json)
        """Respond to incoming calls with a simple text message."""
        # Start our TwiML response
        resp = MessagingResponse()

        # Add a message
        resp.message("The Robots are coming! Head for the hills!")
        # Grab the relevant phone numbers.
        # from_number = request.form['From']
        # to_number = request.form['To']
        # print the body of the text
        print(request.form['Body'])
        # client.messages.create(to=from_number, from_=to_number, messaging_service_sid='MGb70920f205e93db71b6269e37e5c22da',body="...")
        return str(resp), 200
    else:
        abort(400)

# end sample code



if __name__ == '__main__':
    flask = Flask(__name__)
    flask.register_blueprint(app, url_prefix='/')

    flask.run()