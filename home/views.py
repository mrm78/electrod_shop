from django.shortcuts import render
from .models import product

def home(req):
    return render(req, 'home.html', {'products':product.objects.all()})
