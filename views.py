from django.shortcuts import render

# Create your views here.

def ad(request):
    return render(request,'order.html')

def us(request):
    return render(request,'user.html')

def home(request):
    return render(request,'home.html')