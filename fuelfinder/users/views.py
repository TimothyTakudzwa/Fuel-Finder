from django.shortcuts import render

def index(request):
    return render('users/index.html')

