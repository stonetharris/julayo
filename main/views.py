from django.shortcuts import redirect, render, get_object_or_404
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



# Create
def create_donation(request):
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            donation = form.save(commit=False)
            donation.user = request.user
            donation.save()
            return redirect('donations_list')
    else:
        form = DonationForm()
    return render(request, 'create_donation.html', {'form': form})

# Read (List)
def donations_list(request):
    donations = Donation.objects.filter(user=request.user)
    return render(request, 'donations_list.html', {'donations': donations})

# Update
def update_donation(request, donation_id):
    donation = get_object_or_404(Donation, id=donation_id, user=request.user)
    if request.method == 'POST':
        form = DonationForm(request.POST, instance=donation)
        if form.is_valid():
            form.save()
            return redirect('donations_list')
    else:
        form = DonationForm(instance=donation)
    return render(request, 'update_donation.html', {'form': form})

# Delete
def delete_donation(request, donation_id):
    donation = get_object_or_404(Donation, id=donation_id, user=request.user)
    if request.method == 'POST':
        donation.delete()
        return redirect('donations_list')
    return render(request, 'delete_donation.html', {'donation': donation})


def index(request):
    context = {}
    # context['success'] = request.GET.get('success')
    # context['checkout'] = request.GET.get('checkout')
    return render(request, 'index.html', context)

class ContactUsView(FormView):
    template_name = 'contact_us.html'
    form_class = ContactUsForm

    def form_valid(self, form):
        instance = form.save()
        context = {
            'name': instance.name,
            'email': instance.email,
            'description': instance.description,
        }

        send_mail(
            'A new message from ' + str(instance.name) + 'has been submitted',
            render_to_string('email.txt', context),
            'insertFromEmailHere@gmail.com',
            ['insertJuliaEmailHere@gmail.com'],
            fail_silently=False,
        )

        send_mail(
            'Thank you for contacting us!',
            render_to_string('email.txt', context),
            'insertJuliaEmailHere@gmail.com',
            [str(instance.email)],
            fail_silently=False,
        )

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('contact_us_success')  # or any other URL name where you want to redirect after successful form submission

# old contact_us():
# def contact_us(request):
#     form_class = ContactUsForm
#     template_name = 'contact_us.html'
#     context = {}

#     def form_valid(self, form):
#         instance = form.save()
#         context = {}
#         context['name'] = instance.name
#         context['email'] = instance.email
#         context['description'] = instance.description


#         send_mail(
#             'A new message from ' + str(instance.name) + 'has been submitted',
#             render_to_string('email.txt', context),
#             'insertFromEmailHere@gmail.com',
#             ['insertJuliaEmailHere@gmail.com'],
#             fail_silently=False,
#         )

#         send_mail(
#             'Quote Request Confirmation - 357 Company',
#             render_to_string('email.txt', context),
#             'insertJuliaEmailHere@gmail.com',
#             [str(instance.email)],
#             fail_silently=False,
#         )
#         return super(contact_us, self).form_valid(form)
#     return render(request, template_name, context)
    
    
    # def form_invalid(self, form):
    #     return super().form_invalid(form)

def current_projects(request):
    context = {}
    # context['success'] = request.GET.get('success')
    # context['checkout'] = request.GET.get('checkout')
    return render(request, 'current_projects.html', context)


def our_team(request):
    context = {}
    # context['success'] = request.GET.get('success')
    # context['checkout'] = request.GET.get('checkout')
    return render(request, 'our_team.html', context)


def our_story(request):
    context = {}
    # context['success'] = request.GET.get('success')
    # context['checkout'] = request.GET.get('checkout')
    return render(request, 'our_story.html', context)