from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    # return HttpResponse("Hello, World. This is Home page")
    return render(request,'index.html')

def about(request):
    # return HttpResponse("Hello, World. This is About page")
     return render(request,'about.html')
def contact(request):
    # return HttpResponse("Hello, World. This is Contact page")
     return render(request,'contact.html')