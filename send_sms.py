from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = '*********************************'
auth_token = '**********************************'
client = Client(account_sid, auth_token)

message = client.messages \
                  .create(
                  body = 'hello world', from_ = '+14157410967', to = "+14152158296")

print(message.sid)
