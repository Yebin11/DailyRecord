from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request, 'dailyrecord/start_page.html')

def loginP(request):
    return render(request, 'dailyrecord/login_page.html')

def joinP(request):
    return render(request, 'dailyrecord/join_page.html')