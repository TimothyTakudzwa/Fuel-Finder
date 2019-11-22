from django import forms
from .models import *
from datetime import timedelta, date
from .utils import *
from django.contrib.auth.models import User

from django.core.exceptions import ValidationError
from .widgets.select_time_widget import *


def UserForm(forms.Form):
    name = forms.CharField(label='First Name(s)', required=True,
                                max_length=30)
    email = forms.CharField(label='Email', required=False, required=True)
    

class ActionForm(forms.Form):
    pass                    



   
