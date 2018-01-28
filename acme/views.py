# from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    # return HttpResponse('hello')
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    return render(request, 'pages/contact.html')