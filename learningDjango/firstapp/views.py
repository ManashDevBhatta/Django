from django.shortcuts import render
from .models import Firstapp,Store
from django.shortcuts import get_object_or_404
from .forms import FirstappForm

# Create your views here.
def all_first(request):
    f = Firstapp.objects.all()
    return render(request, 'firstapp/all_first.html', {'f':f})



def first_detail(request, item_id):
    first = get_object_or_404(Firstapp, pk=item_id)
    return render(request, 'firstapp/first_detail.html', {'first': first})

def first_store_view(request):
    stores =  None
    if request.method == 'POST':
        form = FirstappForm(request.POST)
        if form.is_valid():
            first_app = form.cleaned_data['first_app']
            stores =  Store.objects.filter(products=first_app)
    else:
        form = FirstappForm()


    return render(request, 'firstapp/first_stores.html',{'stores':stores,'form':form})