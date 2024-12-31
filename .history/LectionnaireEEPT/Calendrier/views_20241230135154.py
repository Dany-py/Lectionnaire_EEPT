from django.shortcuts import render

# Create your views here.

def ho(request):
  return render(request, 'Accueil.html')