from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Booking

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    phone = forms.CharField(
        max_length=15,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Enter your phone number'})
    )

    class Meta:
        model = Booking
        fields = ['route', 'booking_date', 'passengers', 'first_name', 'last_name', 'email', 'phone']
