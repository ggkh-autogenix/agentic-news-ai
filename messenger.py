from twilio.rest import Client
import os



def send_whatsapp(message: str):
    client = Client(os.getenv("TWILIO_ACCOUNT_SID"), os.getenv("TWILIO_AUTH_TOKEN"))
    client.messages.create(
        body=message,
        from_=os.getenv("TWILIO_PHONE"),
        to=os.getenv("TO_PHONE")
    )
