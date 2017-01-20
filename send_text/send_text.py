# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import TwilioRestClient

# Find these values at https://twilio.com/user/account
account_sid = "ACb808038f4d067b9bd0d56e63f99823a9"
auth_token = "9731e25ec124b0886533a04fab71cdbb"
client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(to="+19177412170", from_="+13472465554",
                                     body="FATHOS")

