from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import BuyerRegisterForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = BuyerRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('finder-home')
    else:
        form = BuyerRegisterForm
    
    return render(request, 'buyer/register.html', {'form': form})
            
