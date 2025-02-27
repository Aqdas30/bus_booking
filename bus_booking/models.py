from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now  
import random
import string
from django.db import models

class BusRoute(models.Model):
    destination = models.CharField(max_length=100, unique=True)
    price_one_way = models.DecimalField(max_digits=6, decimal_places=2)
    price_round_trip = models.DecimalField(max_digits=6, decimal_places=2)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.destination}"


class Booking(models.Model):
    BOOKING_STATUS = (
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    )

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    route = models.ForeignKey(BusRoute, on_delete=models.CASCADE)
    passengers = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    booking_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=BOOKING_STATUS, default='pending')
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    booking_reference = models.CharField(max_length=10, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.booking_reference:
            self.booking_reference = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        if self.route:
            self.total_price = (self.passengers * float(self.route.price_one_way))
        super().save(*args, **kwargs)



    def __str__(self):
        return f"{self.booking_reference} - {self.route.destination}"
