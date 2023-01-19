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
from django.views.generic.edit import CreateView

# Create your views here.


def index(request):
    context = {}
    # context['success'] = request.GET.get('success')
    # context['checkout'] = request.GET.get('checkout')
    return render(request, 'index.html', context)


def contact_us(request):
    form_class = ContactUsForm
    template_name = 'contact_us.html'
    context = {}

    def form_valid(self, form):
        instance = form.save()
        context = {}
        context['name'] = instance.name
        context['email'] = instance.email
        context['description'] = instance.description


        send_mail(
            'A new message from ' + str(instance.name) + 'has been submitted',
            render_to_string('email.txt', context),
            'insertFromEmailHere@gmail.com',
            ['insertJuliaEmailHere@gmail.com'],
            fail_silently=False,
        )

        send_mail(
            'Quote Request Confirmation - 357 Company',
            render_to_string('email.txt', context),
            'insertJuliaEmailHere@gmail.com',
            [str(instance.email)],
            fail_silently=False,
        )
        return super(contact_us, self).form_valid(form)
    return render(request, template_name, context)
    
    
    # def form_invalid(self, form):
    #     return super().form_invalid(form)