from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField
from .models import *
from .models import Donation


User = get_user_model()


class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ['amount', 'message']


class ContactUsForm(forms.ModelForm):
    name = forms.CharField(label="Your Name", widget=forms.TextInput(attrs={'class': 'sm:text-xl my-3 rounded-xl text-white text-xs transition ease-in-out w-full bg-gray-700'}))
    email = forms.EmailField(label="Your Email", max_length=60, widget=forms.TextInput(attrs={'class': 'text-xl my-3 rounded-xl text-white text-sm transition ease-in-out w-full bg-gray-700'}))
    description = forms.CharField(label="Please leave a message.", required=False, widget=forms.Textarea(attrs={'class': 'text-xl my-3 rounded-xl text-white text-sm transition ease-in-out w-full bg-gray-700'}))
    class Meta:
        model = ContactUs
        fields = ['name', 'email', 'description']


# class CustomUserCreationForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ("username",)
#         field_classes = {'username': UsernameField}