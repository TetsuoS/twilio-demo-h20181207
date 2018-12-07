import os
from urllib.parse import urlencode
 
from twilio.rest import Client
 
# Environment Setting
os.environ['TWILIO_ACCOUNT'] = "cccccccccccccccc"
os.environ['TWILIO_TOKEN'] = "aaaaaaaaaaaaaaaaaaaaa"
os.environ['TWILIO_PHONE'] = "+81yyyyyyyy"
os.environ['ALERT_PHONE'] = "+81xxxxx"

 
def handler(event, context):
    client = Client(
        os.environ['TWILIO_ACCOUNT'],
        os.environ['TWILIO_TOKEN'],
    )
 
    call = client.calls.create(
        to=os.environ['ALERT_PHONE'],
        from_=os.environ['TWILIO_PHONE'],
        url='http://twimlets.com/message?{}'.format(urlencode({
            'Message[0]': "Hello world",
        })),
    )
 
    print(call.sid)
