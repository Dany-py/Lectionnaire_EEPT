
from django.urls import path
from Calendrier import views

app_name = 'Calendrier'

urlpatterns = [
    path('', views.home, name='home'),
    "path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('find_code/', views.find_code, name = 'find_code'),
    path('api_request_view/', views.api_request_view, name = 'api_request_view'),
    path('contact/send_contact_message/', views.send_contact_message, name = 'send_contact_message')
]