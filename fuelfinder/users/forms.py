from datetime import timedelta, date

from django import forms
#from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import *
from supplier.models import *

from .utils import *
from .widgets.select_time_widget import *

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileForm(forms.Form):
    first_name = forms.CharField(label="First Name", required=True, max_length=100)
    last_name = forms.CharField(label="Last Name", required=True, max_length=100)
    email = forms.EmailField(required=False)
    user = forms.ModelChoiceField(empty_label="-----", required=True, queryset=User.objects.all(), label='Pick A User',)
    supplier_contact = forms.ModelChoiceField(empty_label="-----", required=True, queryset=SupplierProfile.objects.all(), label='Pick A Supplier')                

class ActionForm(forms.Form):
    pass                    



   
