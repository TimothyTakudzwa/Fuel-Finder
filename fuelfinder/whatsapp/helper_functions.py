from django.shortcuts import render 
import requests 
from .constants import * 

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
    if message.lower(0) == 'menu' and user.stage != 'registration':
        return requests_handler
    if user.stage == 'registration':
        response_message = registration_handler(user, message)
    elif user.stage == 'requesting':
        response_message = requests_handler(user, message)
    else:
        response_message = ''
    return response_message

def registration_handler(user, message):
    if user.position == 1:
        full_name = user.first_name + user.last_name
        response_message = greetings_message.format(full_name)
        user.position = 2
        user.save()
    elif user.position == 2: 
        if message.lower() == 'yes':
            response_message = successful_integration
            user.stage= 'requesting'
            user.save()
        else: 
            response_message = "Unfortunately you will have to contact your admin to make changes, but for the time being er eill block this account"
            user.stage = 'blocked'
            user.save()
    return response_message

def requests_handler(user, message): 
    if user.position == 1: 
        pass 
    return ''
