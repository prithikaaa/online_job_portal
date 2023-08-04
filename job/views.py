from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    jobs=Jobs.objects.filter(status=0)
    comp = {'jobs':jobs}
    return render(request, "index.html", comp)
def offers(request):
    category = Category.objects.filter(status=0)
    context = {'category':category}
    return render(request, "offers.html", context)