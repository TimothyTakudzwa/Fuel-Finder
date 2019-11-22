from django.urls import path
from . import views 

urlpatterns = [
    path('', views.base, name='finder-home'),
    path('/index', views.base, name='finder-index'),
]
