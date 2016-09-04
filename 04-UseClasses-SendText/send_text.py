# -*- coding: utf-8 -*-

# Este programa estaba destinado a crear una cuenta en twilio y hacer que se mandara
# un mensaje a nuestro teléfono celular por medio del teléfono que provee twilio al
# tener una cuenta, desafortunadamente parece que twilio no soporta el servicio de aquí
# o no tiene soporte para el operador "Claro"
from twilio.rest import TwilioRestClient

account_sid = "{{ account_sid }}" # Your Account SID from www.twilio.com/console
auth_token  = "{{ auth_token }}"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Hello from Python",
    to="+12345678901",    # Replace with your phone number
    from_="+12345678901") # Replace with your Twilio number

print(message.sid)
