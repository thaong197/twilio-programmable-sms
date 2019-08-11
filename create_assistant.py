from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACef98e9bafdcd986c65d3aa7a02ad1898'
auth_token = 'afb029370cd6e2b9f2dffb3f40e62207'
client = Client(account_sid, auth_token)

assistant = client.autopilot \
                  .assistants \
                  .create(
                       friendly_name='Quickstart Assistant',
                       unique_name='quickstart-assistant'
                   )

print(assistant.sid)
