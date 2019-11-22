from django.shortcuts import render 
import requests 

def send_message(phone_number, message):
    payload = {
        "phone" : phone_number,
        "body" : message
    }
    url = "https://eu33.chat-api.com/instance78632/sendMessage?token=sq0pk8hw4iclh42b"
    r = requests.post(url=url, data=payload)
    print(r)
    return r.status_code


def bot_action(user, message):
    if user.stage == 'registration':
        response_message = registration_handler(user, message)
    elif user.stage == 'requesting':
        response_message = requests_handler(user, message)
    else:
        response_message = ''
    return response_message

def  