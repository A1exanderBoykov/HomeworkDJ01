from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'main/index.html')

def new(request):
    return render(request, 'main/new.html')

def new2(request):
    return render(request, 'main/new2.html')

def new3(request):
    return render(request, 'main/new3.html')
