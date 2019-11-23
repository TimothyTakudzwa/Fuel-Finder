from datetime import timedelta, date

from django import forms
#from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import *
from supplier.models import *
from django.contrib.auth.models import User
from users.models import *

from .utils import *
from .widgets.select_time_widget import *


def validate_user_email(value):
    safe = True
    if '@' in value:
        if User.objects.filter(email=value.strip()).exists():
            safe = False
    if not safe:
        raise ValidationError('%(value)s is already registered',
            params={'value': value},)

class SupplierContactForm(forms.Form):
    first_name = forms.CharField(label='First Name(s)', required=True,
                                max_length=30)
    last_name = forms.CharField(label='Last Name(s)', required=True,
                                 max_length=30)
    email = forms.EmailField(required=True, max_length=100,
                            validators=[validate_user_email])
    cellphone = forms.CharField(label='Cellphone number', required=True,
                                 max_length=100)
    telephone = forms.CharField(label='Telephone number', max_length=100,
                                required=False)
    password = forms.CharField(label='Password', required=True, max_length=100,
                             widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password Confirm', required=True,
                             widget=forms.PasswordInput, max_length=100)

    def clean(self):
        cleaned_data = super(OrganisationUserForm, self).clean()
        password = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")
        if password != password2:
            raise forms.ValidationError("The passwords do not match!")
class ActionForm(forms.Form):
    pass                    



   
