from django.shortcuts import render
from .models import Firstapp
from django.shortcuts import get_object_or_404

# Create your views here.
def all_first(request):
    f = Firstapp.objects.all()
    return render(request, 'firstapp/all_first.html', {'f':f})


# def first_detail(request, item_id):
#     first = get_object_or_404(Firstapp, pk=item_id)
#     return render(request,'firstapp/first_detail.html',{'first':first})

def first_detail(request, item_id):
    first = get_object_or_404(Firstapp, pk=item_id)
    return render(request, 'firstapp/first_detail.html', {'first': first})
