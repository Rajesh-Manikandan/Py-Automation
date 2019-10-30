client = Client(account_sid, auth_token)

message = client.messages.create(
    body='Hello there!',
    from_='whatsapp:+14155238886',
    to='whatsapp:+918072739891'
)

print(message.sid)
