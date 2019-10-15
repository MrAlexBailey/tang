from django.conf.urls import url
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'story/$', views.engagement, name='engagement'),
    url(r'party/$', views.party, name='party'),
    url(r'directions/$', views.directions, name='directions'),
    url(r'activities/$', views.activities, name='activities'),
    url(r'pictures/$', views.pictures, name='pictures'),
    url(r'honeymoon/$', views.honeymoon, name='honeymoon'),
    url(r'rsvp/$', views.rsvp, name='rsvp'),
    url(r'registry/$', views.registry, name='registry'),
    url(r'paypal/$', csrf_exempt(views.paypal), name='paypal'),
    url(r'thanks/$', views.thanks, name='thanks'),
    url(r'europe/$', views.europe, name='europe'),
    url(r'europe/germany/$', views.germany, name='germany'),
    url(r'europe/paris$', views.paris, name='paris'),
    url(r'europe/zurich$', views.zurich, name='zurich')
]