
from django.urls import path
from Calendrier import views

app_name = 'Calendrier'

urlpatterns = [
    path('', views.home, name='home'),

]