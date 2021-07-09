from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request, 'dailyrecord/start_page.html')

def header(request):
    return render(request, 'dailyrecord/header.html')