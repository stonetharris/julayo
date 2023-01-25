from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth import views as auth_views
# from rest_framework import routers


urlpatterns = [
    path('', views.index, name="index"),
    path('contact_us/', views.contact_us, name="contact_us"),
    path('current_projects/', views.current_projects, name="current_projects"),
    path('our_team/', views.our_team, name="our_team"),
    path('our_story/', views.our_story, name="our_story"),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)