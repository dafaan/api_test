from django.shortcuts import render
from django.http import HttpResponse
from .models import item
# Create your views here.
def home(request):
    items = item.objects.all()
    context = {'items':items}
    return render(request, 'index.html', context)

def more(request):
    items = item.objects.all()
    context = {'items':items}
    return render(request, 'shop.html', context)

def contact(request):
    return render(request, 'contact.html')

