from django.contrib.auth import authenticate, update_session_auth_hash, login, logout
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import BadHeaderError, EmailMultiAlternatives
from django.contrib import messages

from datetime import date

from .forms import PasswordChangeForm, RegistrationForm, RegistrationProfileForm,\
    RegistrationEmailForm, UserUpdateForm, ProfilePictureUpdateForm, ProfileUpdateForm, FuelRequestForm
from .models import SupplierProfile, Province, FuelUpdate, FuelRequest


# today's date
today = date.today()


def register(request):
    context = {
        'title': 'Fuel Finder | Register',
    }
    return render(request, 'supplier/accounts/register.html', context=context)


def verification(request, token, user_id):
    context = {
        'title': 'Fuel Finder | Verification',
    }
    return render(request, 'supplier/accounts/verification.html', context=context)


def sign_in(request):
    context = {
        'title': 'Fuel Finder | Login',
    }
    return render(request, 'supplier/accounts/login.html', context=context)


@login_required()
def change_password(request):
    context = {
        'title': 'Fuel Finder | Change Password',
    }
    return render(request, 'supplier/accounts/change_password.html', context=context)


@login_required()
def account(request):
    context = {
        'title': 'Fuel Finder | Account',
    }
    return render(request, 'supplier/accounts/account.html', context=context)


@login_required()
def fuel_request(request):
    context = {
        'title': 'Fuel Finder | Account',
    }
    return render(request, 'supplier/accounts/fuel_request.html', context=context)

