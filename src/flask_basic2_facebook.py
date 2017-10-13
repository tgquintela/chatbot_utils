
"""


https://github.com/davidchua/pymessenger/blob/master/examples/echo_bot.py

Better option
https://github.com/rehabstudio/fbmessenger
https://github.com/rehabstudio/fbmessenger/blob/master/example/main.py

"""
from pymessager.message import Messager
client = Messager(config.facebook_access_token)

import json

from flask import Flask, request

API_ROOT = 'api/'
FB_WEBHOOK = 'fb_webhook'

app = Flask(__name__)


@app.route(API_ROOT + FB_WEBHOOK, methods=["GET"])
def fb_webhook():
    verification_code = 'I_AM_VERIFICIATION_CODE'
    verify_token = request.args.get('hub.verify_token')
    if verification_code == verify_token:
        return request.args.get('hub.challenge')


@app.route(API_ROOT + FB_WEBHOOK, methods=['POST'])
def fb_receive_message():
    message_entries = json.loads(request.data.decode('utf8'))['entry']
    for entry in message_entries:
        for message in entry['messaging']:
            if message.get('message'):
                print("{sender[id]} says {message[text]}".format(**message))
    return "Hi"


if __name__ == '__main__':
    context = ('ssl/fullchain.pem', 'ssl/privkey.pem')
    app.run(host='0.0.0.0', debug=True, ssl_context=context)
