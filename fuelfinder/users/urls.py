from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path('index/', views.index, name="home"),
    path('addUser/', views.supplier_user_create, name="addUser"),
    # path('/index/', views.index, name="home")
    # path('/index/', views.index, name="home")

]