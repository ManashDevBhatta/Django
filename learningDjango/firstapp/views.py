from django.shortcuts import render
from .models import Firstapp

# Create your views here.
def firstapp(request):
    f = Firstapp.objects.all()
    return render(request, 'firstapp/firstapp.html', {'f':f})