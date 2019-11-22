from django.urls import path
from .import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('logout/', auth_views.LogoutView.as_view(template_name='supplier/accounts/logout.html'), name='logout'),

    path('register/', views.register, name='register'),
    path('verification/<token>/<user_id>', views.verification, name='verification'),
    path('login/', views.sign_in, name='login'),
    path('password-change/', views.change_password, name='change-password'),
    path('account/', views.account, name='account'),
    path('fuel-request/', views.fuel_request, name='fuel-request'),


    path('password-reset/',
         auth_views.PasswordResetView.as_view(template_name='supplier/password/password_reset.html'),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='supplier/password/password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='supplier/password/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='supplier/password/password_reset_complete.html'),
         name='password_reset_complete'),

]

