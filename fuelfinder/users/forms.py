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

class UserForm(forms.ModelForm):
    class Meta():
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileForm(forms.Form):
    '''
    class Meta():
        model = SupplierProfile
        fields = ('first_name', 'last_name', 'email')
    '''
    model = SupplierProfile
    first_name = forms.CharField(label="First Name", required=True, max_length=100)
    last_name = forms.CharField(label="Last Name", required=True, max_length=100)
    email = forms.EmailField(required=False)
    #user = forms.ModelChoiceField(empty_label="-----", required=True, queryset=User.objects.all(), label='Pick A User',)
    supplier_contact = forms.ModelChoiceField(empty_label="-----", required=True, queryset=SupplierProfile.objects.all(), label='Pick A Supplier')                
    
    '''def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("Username is taken")
        return username
    '''

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("email is taken")
        return email

    '''def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password2 != password:
            raise forms.ValidationError("Passwords must match.")
        return data
    ''' 
class ActionForm(forms.Form):
    pass                    



   
