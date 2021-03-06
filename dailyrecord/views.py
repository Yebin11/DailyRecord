from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request, 'dailyrecord/start_page.html')

def loginP(request):
    return render(request, 'dailyrecord/login_page.html')

def findInfoP(request):
    return render(request, 'dailyrecord/popup_findinfo.html')

def joinP(request):
    return render(request, 'dailyrecord/join_page.html')

def header(request):
    return render(request, 'dailyrecord/header.html')

def mypage(request):
    return render(request, 'dailyrecord/mypage.html')

def pw_reset(request):
    return render(request, 'dailyrecord/pw_reset.html')

def write(request):
    return render(request, 'dailyrecord/write.html')

def reward(request):
    return render(request, 'dailyrecord/reward.html')

def calendar(request):
    return render(request, 'dailyrecord/calendar.html')

def search(request):
    return render(request, 'dailyrecord/search.html')
