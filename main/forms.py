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
    name = forms.CharField(label="Your Name", widget=forms.TextInput(attrs={'class': 'sm:text-xl my-3 rounded-xl text-black text-xs transition ease-in-out w-full'}))
    email = forms.EmailField(label="Your Email", max_length=60, widget=forms.TextInput(attrs={'class': 'text-xl my-3 rounded-xl text-black text-sm transition ease-in-out w-full'}))
    description = forms.CharField(label="Please leave a message.", required=False, widget=forms.Textarea(attrs={'class': 'text-xl my-3 rounded-xl text-black text-sm transition ease-in-out w-full'}))
    class Meta:
        model = ContactUs
        fields = ['name', 'email', 'description']

class VolunteerForm(forms.Form):
    name = forms.CharField(
        label='Your Name', 
        max_length=100, 
        widget=forms.TextInput(attrs={
            'class': 'text-base my-3 rounded-xl text-black px-4 py-2 transition ease-in-out w-full border border-gray-300'
        })
    )
    email = forms.EmailField(
        label='Email', 
        widget=forms.TextInput(attrs={
            'class': 'text-base my-3 rounded-xl text-black px-4 py-2 transition ease-in-out w-full border border-gray-300'
        })
    )
    description = forms.CharField(
        label="Please leave a message.", 
        required=False, 
        widget=forms.Textarea(attrs={
            'class': 'text-base my-3 rounded-xl text-black px-4 py-2 transition ease-in-out w-full border border-gray-300'
        })
    )
    # interest = forms.ChoiceField(
    #     choices=[('marketing', 'Marketing'), ('fundraising', 'Fundraising'), ('other', 'Other')],
    #     label='Area of Interest'
    # )

class NewsletterForm(forms.Form):
    name = forms.CharField(
        label='Your Name', 
        max_length=100, 
        widget=forms.TextInput(attrs={
            'class': 'sm:text-xl my-3 rounded-xl text-black text-xs transition ease-in-out w-full border border-gray-300 focus:border-green-500'
        })
    )
    email = forms.EmailField(
        label='Your Email', 
        widget=forms.TextInput(attrs={
            'class': 'sm:text-xl my-3 rounded-xl text-black text-xs transition ease-in-out w-full border border-gray-300 focus:border-green-500'
        })
    )




# class CustomUserCreationForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ("username",)
#         field_classes = {'username': UsernameField}