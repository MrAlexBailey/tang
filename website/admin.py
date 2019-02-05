from django.contrib import admin

# Register your models here.
from website.models import *


class RegistryAdmin(admin.ModelAdmin):
    fields = ['order', 'active', 'title', 'description', 'image_name', 'button', 'amount_needed']
    list_display = ['title', 'order', 'active']

class DonationAdmin(admin.ModelAdmin):
    readonly_fields = ['date_time', 'transaction_id']
    fields = ['item', 'amount', 'firstName', 'lastName', 'email', 'address', 'note', 'date_time', 'transaction_id']
    list_display = ['transaction_id', 'full_name', 'item', 'amount',  'date_time']
    list_filter = ['item']

admin.site.register(RegistryItem, RegistryAdmin)
admin.site.register(Donation, DonationAdmin)