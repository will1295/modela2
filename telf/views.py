from django.shortcuts import render
from .models import Celular

# Create your views here.

def Lista(request):
    listado = Celular.objects.all()
    return render(request,"celulares.html",{"celular":listado})