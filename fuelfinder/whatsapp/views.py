from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Profile

def index(request):
    token = request.GET.get('token')
    data = request.json 
    message = data['messages']['body']
    phone_number = data['message']['chatid'].split('@')[0]
    if token != 'sq0pk8hw4iclh42b':
        return 'Unathorized'
    else:
        check = Profile.objects.filter(phone_number = phone_number).exists()
        if check:
            user = Profile.get(phone_number=phone_number)
            response_message = bot_action(user, message)
        else:
            response_message = "We could not find an account associated with you"    
    