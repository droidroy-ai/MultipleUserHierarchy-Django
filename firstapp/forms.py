from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser, Contact, Seller, SellerAdditional
from django import forms
from django.core.validators import RegexValidator

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('email',)

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email',)

class ContactUsForm(forms.ModelForm):
    # email = forms.EmailField(required=True)
    # name = forms.CharField(max_length=20, required=True)
    # phone_regex = RegexValidator(regex=r'^\+?1?\d{14}$', message="the format : '+919163862585'. Upto 14 digits allowed.")
    # phone = forms.CharField(max_length=255, required=True, validators=[phone_regex])
    # query = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Contact
        fields = [
            'email', 
            'name',
            'phone',
            'query',
        ]

class RegistrationFormBasic(UserCreationForm):
    class Meta:
        model = Seller
        fields = [
            'email',
            'name', 
            'password1',
            'password2',
        ]

# class RegistrationFormSeller(UserCreationForm):
#     gst = forms.CharField(max_length=10)
#     warehouse_location = forms.CharField(max_length=1000)

#     class Meta:
#         model = Seller
#         fields = [
#             'email',
#             'name', 
#             'password1',
#             'password2',
#             'gst',
#             'warehouse_location'
#         ]

class RegistrationFormSeller(forms.ModelForm):
    class Meta:
        model = SellerAdditional
        fields = [
            'gst',
            'warehouse_location'
        ]