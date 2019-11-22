from django.contrib.auth import authenticate, update_session_auth_hash, login, logout
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import BadHeaderError, EmailMultiAlternatives
from django.contrib import messages
import secrets

from datetime import date

from .forms import PasswordChange, RegistrationForm, RegistrationProfileForm,\
    RegistrationEmailForm, UserUpdateForm, ProfilePictureUpdateForm, ProfileUpdateForm, FuelRequestForm
from .models import SupplierProfile, Province, FuelUpdate, FuelRequest, Transaction, Rating, TokenAuthentication
from ..whatsapp.models import BuyerProfile


# today's date
today = date.today()


def register(request):
    context = {
        'title': 'Fuel Finder | Register',
        'email': RegistrationEmailForm(),
        'registration': RegistrationForm()
    }
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 == pass2:
            User.objects.create_user(username=username, email=email, password=pass1)

            user = User.objects.get(username=username)
            user.is_active = False
            user.save()
            
            token = secrets.token_hex(12)
            TokenAuthentication.objects.create(user=request.user, key=token)

            domain = request.get_host()
            url = f'{domain}/verification/{token}/{user.id}'

            sender = f'Fuel Finder Accounts<tests@marlvinzw.me>'
            subject = 'User Registration'
            message = f"Dear {username} , complete signup here : \n {url} \n. Your password is {pass1}"
            
            try:
                msg = EmailMultiAlternatives(subject, message, sender, [f'{email}'])
                msg.send()

                messages.success(request, f"{username} Registered Successfully")
                return redirect('dashboard')

            except BadHeaderError:
                messages.warning(request, f"Oops , Something Wen't Wrong, Please Try Again")
                return redirect('register')       
        else:
            messages.warning(request, "Passwords don't match")
            return redirect('register')
    return render(request, 'supplier/accounts/register.html', context=context)


def verification(request, token, user_id):
    context = {
        'title': 'Fuel Finder | Verification',
    }
    token_check = TokenAuthentication.objects.filter(key=token).exists()
    if token_check:
        user_check = TokenAuthentication.objects.get(key=token, user__id=user_id).exists()
        if user_check:
            user = User.objects.filter(id=user_id)
            user.is_active = True
            user.save()
            messages.success(request, 'Verification Success')
            return redirect('login')
        else:
            messages.warning(request, "Username doesn't exist")
            return redirect('login')
    else:
        messages.warning(request, 'Wrong Token')
        return redirect('login')
    return render(request, 'supplier/accounts/verification.html', context=context)


def sign_in(request):
    context = {
        'title': 'Fuel Finder | Login',
    }
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        authenticated = authenticate(username=username, password=password)
        if authenticated:
            client = User.objects.get(username=username)
            login(request, client)

            messages.success(request, 'Welcome {client.username}')
            return redirect('dashboard')
        else:
            messages.warning(request, 'Incorrect username or password')
            return redirect('login')

    return render(request, 'supplier/accounts/login.html', context=context)


@login_required()
def change_password(request):
    context = {
        'title': 'Fuel Finder | Change Password',
        'password_change': PasswordChange(user=request.user)
    }
    if request.method == 'POST':
        old = request.POST.get('old_password')
        new1 = request.POST.get('new_password1')
        new2 = request.POST.get('new_password2')

        if authenticate(request, username=request.user.username, password=old):
            if new1 != new2:
                messages.warning(request, "Passwords Don't Match")
                return redirect('change-password')
            else:
                user = request.user
                user.set_password(new1)
                user.save()
                update_session_auth_hash(request, user)

                messages.success(request, 'Password Successfully Changed')
                return redirect('dashboard')
        else:
            messages.warning(request, 'Wrong Old Password, Please Try Again')
            return redirect('change-password')
    return render(request, 'supplier/accounts/change_password.html', context=context)


@login_required()
def account(request):
    context = {
        'title': 'Fuel Finder | Account',
        'user': UserUpdateForm(instance=request.user)

    }
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, f'Profile successfully updated')
            return redirect('account')
        else:
            messages.warning(request, f'Something went wrong while saving your changes')
            return redirect('account')
    return render(request, 'supplier/accounts/account.html', context=context)


@login_required()
def fuel_request(request):
    context = {
        'title': 'Fuel Finder | Account',
        'requests': FuelRequest.objects.filter(date=today)
    }
    if request.method == 'POST':
        submitted_id = request.POST.get('request_id')
        if FuelRequest.objects.filter(id=submitted_id).exists():
            request_id = FuelRequest.objects.get(id=submitted_id)
            buyer_id = BuyerProfile.objects.get(id=request.user)
            Transaction.objects.create(request_id=request_id,
                                       buyer_id=buyer_id)
            messages.success(request, f'You have accepted a request for {request_id.amount} litres from {buyer_id.name}')
            return redirect('fuel-request')
    else:
        messages.warning(request, 'Oops something just went wrong')
        return redirect('fuel-request')
    return render(request, 'supplier/accounts/fuel_request.html', context=context)

