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

def call():
    from twilio.rest import Client
# Your Account Sid and Auth Token from twilio.com/console
    account_sid = 'AC4100c72954a1f9949fc4700a8d0594bb'
    auth_token = 'e1529115d0f1a57b6b8e6b17644f6087'
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body="The user is requesting a call",
                        from_='+19496196487',
                        to='+919930035998'
                    )

    print(message.sid)