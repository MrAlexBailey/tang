from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def slim_trim(request):
    return request.GET.get('slim', None) == 'True'

def index(request):
    return render(request, 'website/home.html')

def party(request):
    slim = slim_trim(request)     
    return render(request, 'website/party.html', {'slim': slim})

def directions(request):
    slim = slim_trim(request)     
    return render(request, 'website/directions.html', {'slim': slim})

def activities(request):
    slim = slim_trim(request)     
    return render(request, 'website/activities.html', {'slim': slim})

def rsvp(request):
    slim = slim_trim(request)     
    return render(request, 'website/rsvp.html', {'slim': slim})

def registry(request):
    slim = slim_trim(request)     
    return render(request, 'website/registry.html', {'slim': slim})