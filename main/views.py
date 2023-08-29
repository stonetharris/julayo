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
from django.template.loader import render_to_string
from django.db.models import Q
from django.views.generic.edit import CreateView
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
import os

import stripe
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY

def donate(request):
    if request.method == 'POST':
        token = request.POST.get('stripeToken')
        amount = int(float(request.POST.get('amount', 0)) * 100)  # convert dollars to cents for Stripe
        try:
            charge = stripe.Charge.create(
                amount=amount,
                currency='usd',
                description='Donation',
                source=token,
            )
            # Save the donation information to the database, send a confirmation email, etc.
            messages.success(request, "Your donation was successful!")
            return redirect('donation_success')

        except stripe.error.CardError as e:
            messages.error(request, "Your card has been declined.")
        except stripe.error.RateLimitError as e:
            # Too many requests made to the API too quickly
            messages.error(request, "Rate limit exceeded. Please try again later.")
        except stripe.error.InvalidRequestError as e:
            # Invalid parameters were supplied to Stripe's API
            messages.error(request, "Invalid parameters. Please contact support.")
        except stripe.error.AuthenticationError as e:
            # Authentication with Stripe's API failed
            messages.error(request, "Authentication failed. Please contact support.")
        except stripe.error.APIConnectionError as e:
            # Network communication with Stripe failed
            messages.error(request, "Network error. Please try again.")
        except stripe.error.StripeError as e:
            # Display a very generic error to the user, and maybe send yourself an email
            messages.error(request, "An error occurred. Please try again or contact support.")
        except Exception as e:
            # Something else happened, completely unrelated to Stripe
            messages.error(request, "An internal error occurred. Please try again later.")
    
    context = {
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
    }
    return render(request, 'donate.html', context)

def donation_success(request):
    return render(request, 'donation_success.html')

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
            'julayomedical@gmail.com',
            ['julayomedical@gmail.com'],
            fail_silently=False,
        )

        send_mail(
            'Thank you for contacting us!',
            render_to_string('email.txt', context),
            'julayomedical@gmail.com',
            [str(instance.email)],
            fail_silently=False,
        )

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('contact_us_success')  # or any other URL name where you want to redirect after successful form submission

def current_projects(request):
    context = {
        'google_maps_api_key': os.environ.get('GOOGLE_MAPS_API_KEY', settings.GOOGLE_MAPS_API_KEY),
    }
    return render(request, 'current_projects.html', context)

def our_team(request):
    context = {}
    return render(request, 'our_team.html', context)

def our_story(request):
    context = {}
    return render(request, 'our_story.html', context)

def gala_event(request):
    context = {}
    return render(request, 'gala_event.html', context)