from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField
from .models import User


User = get_user_model()


# class ContactUsModelForm(forms.ModelForm):
#     class Meta:
#         model = NewUser
#         fields = (
#             'first_name',
#             'last_name',
#         )