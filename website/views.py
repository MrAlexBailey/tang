from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'website/home.html')

def party(request):
    return render(request, 'website/party.html')

def directions(request):
    return render(request, 'website/directions.html')

def activities(request):
    return render(request, 'website/activities.html')

def rsvp(request):
    return render(request, 'website/rsvp.html')

def registry(request):
    return render(request, 'website/registry.html')