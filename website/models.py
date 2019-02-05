from __future__ import unicode_literals

from django.db import models

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

class Donation(models.Model):
    item = models.ForeignKey('RegistryItem', on_delete=models.SET_NULL, null=True)
    amount = models.FloatField()
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    address = models.TextField()
    note = models.TextField()
    transaction_id = models.CharField(max_length=100, default='N/A')
    date_time = models.DateTimeField(auto_now_add=True)

    def full_name(self):
        return '{}, {}'.format(self.lastName, self.firstName)