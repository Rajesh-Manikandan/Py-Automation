# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACf43ca24df5abbe02436e488f64b7aaa6'
auth_token = '987eb0f4a47b8eca28893a4aaaf479bf'
client = Client(account_sid, auth_token)

message = client.messages.create(
    body='Hello there!',
    from_='whatsapp:+14155238886',
    to='whatsapp:+918072739891'
)

print(message.sid)
