from twilio.rest import Client
import os

account_sid = os.getenv("TWILIO_SID")
auth_token = os.getenv("TWILIO_TOKEN")
twilio_number = os.getenv("TWILIO_WHATSAPP")

client = Client(account_sid, auth_token)

def send_whatsapp(to_number, message):
    client.messages.create(
        body=message,
        from_=f'whatsapp:{twilio_number}',
        to=f'whatsapp:{to_number}'
    )
