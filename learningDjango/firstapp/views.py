from django.shortcuts import render
from .models import Firstapp
from django.shortcuts import get_object_or_404

# Create your views here.
def firstapp(request):
    f = Firstapp.objects.all()
    return render(request, 'firstapp/firstapp.html', {'f':f})


def firstapp_detail(request, item_id):
    first = get_object_or_404(Firstapp, pk=item_id)
    return render(request,'firstapp/firstapp_detail.html',{'first':first})

