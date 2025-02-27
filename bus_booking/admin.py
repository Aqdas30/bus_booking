from django.contrib import admin
from .models import Booking, BusRoute
# Register your models here.
admin.site.register(BusRoute)
admin.site.register(Booking)