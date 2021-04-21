from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.Index.as_view(), name="index"),
    path("contactus/", views.ContactUs.as_view(), name="contactus"),

    
    path("signup/", views.RegisterViewBasic.as_view(), name="signup"),
    path("login/", views.LoginViewUser.as_view(), name="login"),
    path("signupseller/", views.RegisterViewSeller.as_view(), name="signupseller"),
    path("logout/", views.LogoutViewUser.as_view(), name="logout"),


    #path("cart/", )
]