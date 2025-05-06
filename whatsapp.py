from twilio.rest import Client
import os

def send_whatsapp(to, message):
    # Trim to 100 words
    words = message.split()
    trimmed_message = ' '.join(words[:100])  # Limit to first 100 words

    account_sid = os.getenv("TWILIO_SID")
    auth_token = os.getenv("TWILIO_TOKEN")
    from_whatsapp_number = os.getenv("TWILIO_WHATSAPP")

    client = Client(account_sid, auth_token)
    client.messages.create(
        body=trimmed_message,
        from_=f'whatsapp:{from_whatsapp_number}',
        to=f'whatsapp:{to}'
    )
