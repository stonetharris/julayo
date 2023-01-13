from django.shortcuts import redirect, render
from django.template import base
# from twilio.rest import Client
from .forms import *
from .models import *
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth import login
from urllib.parse import urlencode
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseRedirect
# from rest_framework.viewsets import ModelViewSet
from django.core.mail import send_mail
# import stripe
from django.template.loader import render_to_string
from django.db.models import Q

# Create your views here.


def index(request):
    context = {}
    # context['success'] = request.GET.get('success')
    # context['checkout'] = request.GET.get('checkout')
    return render(request, 'index.html', context)