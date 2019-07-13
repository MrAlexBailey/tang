from django.contrib import admin

# Register your models here.
from website.models import *
from django.urls import reverse
from django.utils.html import format_html


class RegistryAdmin(admin.ModelAdmin):
    fields = ['order', 'active', 'title', 'description', 'image_name', 'button', 'amount_needed']
    list_display = ['title', 'amount_needed', 'amount_remaining', 'order', 'active']
    
    


class DonationAdmin(admin.ModelAdmin):
    readonly_fields = ['date_time', 'transaction_id']
    fields = ['item', 'amount', 'firstName', 'lastName', 'email', 'address', 'note', 'date_time', 'transaction_id', 'verified']
    list_display = ['transaction_id', 'full_name', 'item', 'amount',  'date_time', 'verified']
    list_filter = ['item', 'verified']
    ordering = ['-date_time']

admin.site.register(RegistryItem, RegistryAdmin)
admin.site.register(Donation, DonationAdmin)