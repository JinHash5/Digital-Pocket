# from twilio.rest import Client

# # Your Account SID from twilio.com/console
# account_sid = "AC4100c72954a1f9949fc4700a8d0594bb"
# # Your Auth Token from twilio.com/console
# auth_token  = "e1529115d0f1a57b6b8e6b17644f6087"

# client = Client(account_sid, auth_token)

# message = client.messages \
# 		.create(
#     to="+919930035998", 
#     from_="+19496196487",
#     body="Hello from Python!")

# print(message.sid)

def call1():
    from twilio.rest import Client
# Your Account Sid and Auth Token from twilio.com/console
    account_sid = 'AC09c050b96951b1bbed41f71ab5f2f472'
    auth_token = '8630c09dff748daf78bcc1436ba2e34a'
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body="The user wants to connect",
                        from_='+14156896062',
                        to='+918655232275'
                    )

    print(message.sid)


def call2():
    from twilio.rest import Client
# Your Account Sid and Auth Token from twilio.com/console
    account_sid = 'AC09c050b96951b1bbed41f71ab5f2f472'
    auth_token = '8630c09dff748daf78bcc1436ba2e34a'
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body="The user wants to call",
                        from_='+14156896062',
                        to='+918879490461'
                    )

    print(message.sid)