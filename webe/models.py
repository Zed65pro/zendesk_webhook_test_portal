from django.db import models

TICKET_STATUS_CLOSED = 'Closed'


class Customer(models.Model):
    name = models.CharField(max_length=255)
    customer_id = models.IntegerField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
