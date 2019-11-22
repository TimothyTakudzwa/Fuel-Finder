from django.shortcuts import render


from supplier.models import *
from supplier.forms import *
from .forms import *

from datetime import datetime

def index(request):
    return render(request, 'users/index.html')

# Begining Of Supplier Management

def supplier_user_create(request):
     
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            #puser = get_object_or_404(User, username='biddingwars')
            # puser = request.user
            # image_name = blog_save_image_upload(request)
            image_name = True 
            if image_name:
                form.save()
                user = User.objects.create(
                    first_name=form.first,name,
                    last_name=form.last_name,
                    email = form.email)
                user.save()    
                contact = SupplierContact(
                    user = user,
                    supplier_profile = form.supplier_profile,
                )
                contact.save()
                messages.success(request, _('Your profile was successfully updated!'))
                return redirect('user:index')
            else:
                msg = "There was an error uploading the image"
                messages.error(request, msg)    
        
        else:
            msg = "Error in Information Submitted"
            messages.error(request, msg)
    else:
        form = ProfileForm()


    return render (request, 'users/add_user.html', {'form': form}) 

def edit_supplier(request,id):
    supplier = get_object_or_404(SupplierProfile, id=id)
    if request.method == "POST":
        form = UserForm(request.POST, request.FILES, instance=supplier)
        if form.is_valid():
            data = form.cleaned_data
            supplier = form.save()
            messages.success(request, 'Changes Successfully Update')
            return redirect('users.index')
    else:
        form = SupplierProfile(instance=supplier)
    return render(request, 'users/supplier_edit.html', {'form': form, 'supplier': supplier})

def delete_user(request,id):
    supplier = get_object_or_404(SupplierProfile, id=id)

    if request.method == 'POST':
        form = ActionForm(request.POST)
        if form.is_valid():
            supplier.delete()
            messages.success(request, 'User Has Been Deleted')
        return redirect('administrator:blog_all_posts')
    form = ActionForm()    

    return render(request, 'user/supplier_delete.html', {'form': form, 'supplier': supplier})










