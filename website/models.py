from __future__ import unicode_literals

from django.db import models
from django.core.mail import send_mail

# Create your models here.
class RegistryItem(models.Model):
    order = models.IntegerField(default=1)
    title = models.CharField(max_length=100)
    description = models.TextField()
    image_name = models.CharField(max_length=50)
    button = models.CharField(max_length=100)
    amount_needed = models.IntegerField()
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def amount_remaining(self):
        total_received = sum(x.amount for x in Donation.objects.filter(item=self))
        return max(0, self.amount_needed - total_received)

class Donation(models.Model):
    item = models.ForeignKey('RegistryItem', on_delete=models.SET_NULL, null=True)
    amount = models.FloatField()
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    address = models.TextField(blank=True)
    note = models.TextField(blank=True)
    transaction_id = models.CharField(max_length=100, default='N/A')
    date_time = models.DateTimeField(auto_now_add=True)
    verified = models.BooleanField(default=False)

    def full_name(self):
        return '{}, {}'.format(self.lastName, self.firstName)

    def save(self, *args, **kwargs):
        new = False
        if not self.pk:
            new = True
        super(Donation, self).save(*args, **kwargs)
        if new:
            message = """New donation received!<br><br>
            <table style="padding: 2px 14px;">
            <tr><td style="text-align: right;padding: 2px 14px;">From</td><td style="padding: 2px 14px;">{} {}</td></tr>
            <tr><td style="text-align: right;padding: 2px 14px;">Goal</td><td style="padding: 2px 14px;">{}</td></tr>
            <tr><td style="text-align: right;padding: 2px 14px;">Amount</td><td style="padding: 2px 14px;">${:.2f}</td></tr>
            <tr><td style="text-align: right;padding: 2px 14px;">Note</td><td style="padding: 2px 14px;">{}</td></tr>
            </table>
            """.format(self.firstName, self.lastName, self.item, float(self.amount), self.note)
            send_mail('New Donation From {} {}'.format(self.firstName, self.lastName), '', 'Registry <registry@alexandmelissabailey.com>', ['mralexbailey@gmail.com', 'melissamariemanson@gmail.com'], html_message=message)