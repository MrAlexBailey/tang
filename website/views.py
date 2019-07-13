from django.shortcuts import render
from django.db.models import Sum
from django.http import HttpResponse
from website.models import *
import tang.secrets
import hashlib
import logging
import urlparse
from urllib import urlencode
from urllib2 import Request, urlopen


def slim_trim(request):
    return request.GET.get('slim', None) == 'True'

def party(request):
    slim = slim_trim(request)     
    return render(request, 'website/party.html', {'slim': slim, 'active': 'party'})

def directions(request):
    slim = slim_trim(request)     
    return render(request, 'website/directions.html', {'slim': slim, 'active': 'directions'})

def activities(request):
    slim = slim_trim(request)     
    return render(request, 'website/activities.html', {'slim': slim, 'active': 'activities'})

def rsvp(request):
    slim = slim_trim(request)     
    return render(request, 'website/rsvp.html', {'slim': slim, 'active': 'rsvp'})

def thanks(request):
    return render(request, 'website/thanks.html')

def registry(request):
    slim = slim_trim(request)
    items = RegistryItem.objects.filter(active=True).order_by('order').annotate(amount_received=Sum('donation__amount'))
    funded = []
    unfunded = []
    for item in items:
        item.amr = max(0, item.amount_needed - max(0, item.amount_received))
        if item.amr == 0:
            item.percent_finished = '100%'
            funded.append(item)
        else:
            finished = 1 - float(item.amr)/float(item.amount_needed)
            if finished < .07 and finished > 0:
                finished = .07
            item.percent_finished = '{:.2%}'.format(finished)
            unfunded.append(item)
    items = unfunded + funded
    return render(request, 'website/registry.html', {'slim': slim, 'active': 'registry', 'items': items})

def engagement(request):
    slim = slim_trim(request)
    return render(request, 'website/engagement.html', {'slim': slim, 'active': 'engagement'})

def paypal(request):
    slim = slim_trim(request)
    logging.info('REQUEST RECEIVED ON PAYPAL')
    if request.method == 'POST':
        logging.info('POST RECEIVED ON PAYPAL')
        logging.info(request.POST)
        if hashlib.sha256(request.POST['custom']).hexdigest() == tang.secrets.HASH:
            item = RegistryItem.objects.get(title=request.POST['item_name'])
            address = request.POST.get('address_street', '') + '\n' + request.POST.get('address_city', '') + ', ' + request.POST.get('address_state', '') + ' ' + request.POST.get('address_zip', '')
            obj = Donation.objects.create(item=item, 
                                    address=address,
                                    amount=request.POST.get('payment_gross', 0),
                                    firstName=request.POST.get('first_name', ''),
                                    lastName=request.POST.get('last_name', ''),
                                    email=request.POST.get('payer_email', ''),
                                    transaction_id=request.POST.get('txn_id', ''),
                                    note=request.POST.get('memo', '')
                                    )
            try:
                params = urlparse.parse_qsl(request.body)
                data = urlencode(params)
                data += '&cmd=_notify-validate'
                headers = {'User-Agent': 'Python-IPN-VerificationScript', 'content-type': 'application/x-www-form-urlencoded'}
                resp = urlopen(Request('https://ipnpb.paypal.com/cgi-bin/webscr', data=data, headers=headers))
                if resp.read() == 'VERIFIED':
                    obj.verified = True
                    obj.save()
            except:
                logging.warning('Verify Failed')

        return HttpResponse('')
    else:
        return render(request, 'website/engagement.html', {'slim': slim, 'active': 'engagement'})

    return HttpResponse('')

def main(request):
    return render(request, 'website/main.html')
    
def error_404(request):
    slim = slim_trim(request)
    return render(request, 'website/engagement.html', {'slim': slim, 'active': 'engagement'}, status=404)

def europe(request):
    return render(request, 'website/europe.html')

def germany(request):
    return render(request, 'website/germany.html')

def paris(request):
    return render(request, 'website/paris.html')

def zurich(request):
    return render(request, 'website/zurich.html')