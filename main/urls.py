from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth import views as auth_views
# from rest_framework import routers
from .views import ContactUsView


urlpatterns = [
    path('', views.index, name="index"),
    # path('contact_us/', views.contact_us, name="contact_us"),
    path('current_projects/', views.current_projects, name="current_projects"),
    path('our_team/', views.our_team, name="our_team"),
    path('our_story/', views.our_story, name="our_story"),
    path('donations/create/', views.create_donation, name='create_donation'),
    path('donations/', views.donations_list, name='donations_list'),
    path('donations/update/<int:donation_id>/', views.update_donation, name='update_donation'),
    path('donations/delete/<int:donation_id>/', views.delete_donation, name='delete_donation'),
    path('contact-us/', ContactUsView.as_view(), name='contact_us'),
    path('donate/', views.donate, name='donate'),
    path('donation_success/', views.donation_success, name='donation_success'),
    path('gala_event/', views.gala_event, name='gala_event'),
    path('flyer/', views.flyer, name='flyer'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)