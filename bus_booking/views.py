from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import BookingForm
from .models import Booking
from django.contrib.auth.decorators import login_required

from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib import messages

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from .forms import BookingForm, CustomUserCreationForm
from .models import Booking, BusRoute
from django.shortcuts import render
from .models import BusRoute

from django.shortcuts import render
from .models import BusRoute



# Mapping destinations to their respective currencies
CURRENCY_MAPPING = {
    "BOSNIA AND HERZEGOVINA": "KM",
    "CROATIA": "EUR",
    "SLOVENIA": "EUR",
    "AUSTRIA": "EUR",
    "SWITZERLAND": "EUR",
    "NETHERLANDS - BELGIUM": "EUR",
    "GERMANY": "EUR",
}

# Mapping destinations to their country
DESTINATION_COUNTRY_MAPPING = {
    "Orasje - Sarajevo": "BOSNIA AND HERZEGOVINA",
    "Orasje - Tuzla": "BOSNIA AND HERZEGOVINA",
    "Orasje - Mostar": "BOSNIA AND HERZEGOVINA",

    "Zagreb": "CROATIA",
    "Rijeka": "CROATIA",
    "Pula": "CROATIA",

    "Maribor": "SLOVENIA",
    "Ljubljana": "SLOVENIA",

    "Graz": "AUSTRIA",
    "Vienna": "AUSTRIA",
    "Salzburg": "AUSTRIA",
    "Villach": "AUSTRIA",
    "Klagenfurt": "AUSTRIA",

    "Bern": "SWITZERLAND",
    "Basel": "SWITZERLAND",
    "Lucerne": "SWITZERLAND",
    "Zurich": "SWITZERLAND",

    "Amsterdam": "NETHERLANDS - BELGIUM",
    "Rotterdam": "NETHERLANDS - BELGIUM",
    "Brussels": "NETHERLANDS - BELGIUM",

    "München": "GERMANY",
    "Ulm": "GERMANY",
    "Stuttgart": "GERMANY",
    "Pforzheim": "GERMANY",
    "Karlsruhe": "GERMANY",
    "Mannheim": "GERMANY",
    "Frankfurt": "GERMANY",
    "Köln": "GERMANY",
    "Düsseldorf": "GERMANY",
    "Duisburg": "GERMANY",
    "Essen": "GERMANY",
    "Dortmund": "GERMANY",
    "Freilassing": "GERMANY",
    "Rosenheim": "GERMANY",
    "Ingolstadt": "GERMANY",
    "Nürnberg": "GERMANY",
    "Kassel": "GERMANY",
    "Göttingen": "GERMANY",
    "Hannover": "GERMANY",
    "Hamburg": "GERMANY",
    "Passau": "GERMANY",
    "Regensburg": "GERMANY",
    "Berlin": "GERMANY",
}
from django.utils.translation import gettext as _
from django.shortcuts import render
from django.utils.translation import gettext as _

def index(request):
    routes = BusRoute.objects.all()
    message = _("Welcome to the Bus Station!")  # Ensure translation is used

    # Dictionary to store grouped routes
    grouped_routes = {
        "BOSNIA AND HERZEGOVINA": [],
        "CROATIA": [],
        "SLOVENIA": [],
        "AUSTRIA": [],
        "SWITZERLAND": [],
        "NETHERLANDS - BELGIUM": [],
        "GERMANY": []
    }

    # Classify routes based on known destinations
    country_mapping = {
        "Orasje - Sarajevo": "BOSNIA AND HERZEGOVINA",
        "Orasje - Tuzla": "BOSNIA AND HERZEGOVINA",
        "Orasje - Mostar": "BOSNIA AND HERZEGOVINA",
        "Zagreb": "CROATIA",
        "Rijeka": "CROATIA",
        "Pula": "CROATIA",
        "Maribor": "SLOVENIA",
        "Ljubljana": "SLOVENIA",
        "Graz": "AUSTRIA",
        "Vienna": "AUSTRIA",
        "Salzburg": "AUSTRIA",
        "Villach": "AUSTRIA",
        "Klagenfurt": "AUSTRIA",
        "Bern": "SWITZERLAND",
        "Basel": "SWITZERLAND",
        "Lucerne": "SWITZERLAND",
        "Zurich": "SWITZERLAND",
        "Amsterdam": "NETHERLANDS - BELGIUM",
        "Rotterdam": "NETHERLANDS - BELGIUM",
        "Brussels": "NETHERLANDS - BELGIUM",
        "München": "GERMANY",
        "Ulm": "GERMANY",
        "Stuttgart": "GERMANY",
        "Pforzheim": "GERMANY",
        "Karlsruhe": "GERMANY",
        "Mannheim": "GERMANY",
        "Frankfurt": "GERMANY",
        "Köln": "GERMANY",
        "Düsseldorf": "GERMANY",
        "Duisburg": "GERMANY",
        "Essen": "GERMANY",
        "Dortmund": "GERMANY",
        "Freilassing": "GERMANY",
        "Rosenheim": "GERMANY",
        "Ingolstadt": "GERMANY",
        "Nürnberg": "GERMANY",
        "Kassel": "GERMANY",
        "Göttingen": "GERMANY",
        "Hannover": "GERMANY",
        "Hamburg": "GERMANY",
        "Passau": "GERMANY",
        "Regensburg": "GERMANY",
        "Berlin": "GERMANY"
    }

    # Assign each route to its country group
    for route in routes:
        country = country_mapping.get(route.destination, "OTHER")
        if country in grouped_routes:
            grouped_routes[country].append(route.destination)

    # ✅ Merge context dictionaries into one
    context = {
        "grouped_routes": grouped_routes,
        "message": message
    }

    return render(request, "index.html", context)

def gallery(request):
    images = [
        "bus1.png", "bus2.jpg", "bus3.png", 
       "bus1.png", "bus2.jpg", "bus3.png", "bus1.png", "bus2.jpg", "bus3.png", 
    ]  
    return render(request, "gallery.html", {"gallery_images": images})

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Registration successful! You can now log in.")
            return redirect("login")
    else:
        form = CustomUserCreationForm()
    return render(request, "register.html", {"form": form})
from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from .models import BusRoute
from datetime import datetime  # ✅ Import datetime for date conversion

from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from .models import BusRoute
import random
import string
from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from .models import BusRoute, Booking
import random
import string
from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from .models import BusRoute, Booking
import traceback
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from datetime import datetime
from .models import BusRoute, Booking
import random, string
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from datetime import datetime
from .models import BusRoute, Booking
import random, string

# Function to generate a booking reference
def generate_booking_reference():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

# Function to dynamically apply discounts
def calculate_discounted_price(route, adults, children, students, retired=0):
    base_price = float(route.price_one_way)

    total_price = (
        (adults * base_price) +  # No discount for adults
        (children * base_price * 0.5) +  # 50% discount for children under 12
        (students * base_price * 0.9) +  # 10% discount for students
        (retired * base_price * 0.9)  # 10% discount for retired persons (if applicable)
    )

    return total_price
def book_ticket(request):
    """Handles the booking process for bus tickets."""
    if request.method == "POST":
        try:
            print("🚀 Received POST data:", request.POST)

            # ✅ Get Destination
            destination_name = request.POST.get("destination", "").strip()
            if not destination_name:
                print("❌ Error: Destination is missing")
                return redirect("bus_booking:index")

            route = get_object_or_404(BusRoute, destination=destination_name)

            # ✅ Get and Parse Booking Date
            booking_date_str = request.POST.get("booking_date", "").strip()
            if not booking_date_str:
                print("❌ Error: Booking date is missing")
                return redirect("bus_booking:index")

            try:
                if "-" in booking_date_str and ":" in booking_date_str:
                    booking_date = datetime.strptime(booking_date_str, "%Y-%m-%d %H:%M").date()
                else:
                    booking_date = datetime.strptime(booking_date_str, "%A, %d %B %Y %H:%M").date()
            except ValueError:
                print(f"❌ Error: Invalid date format received: {booking_date_str}")
                return redirect("bus_booking:index")

            # ✅ Get Passenger Details
            try:
                adults = int(request.POST.get("adults", "0"))
                children = int(request.POST.get("children", "0"))
                students = int(request.POST.get("students", "0"))
                retired = int(request.POST.get("retired", "0"))  # Optional retired category
            except ValueError:
                print("❌ Error: Passenger count conversion failed")
                return redirect("bus_booking:index")

            total_passengers = adults + children + students + retired
            if total_passengers == 0:
                print("❌ Error: No passengers selected!")
                return redirect("bus_booking:index")

            print(f"✅ Passengers count - Adults: {adults}, Children: {children}, Students: {students}, Retired: {retired}, Total: {total_passengers}")

            # ✅ Get User Details
            first_name = request.POST.get("first_name", "").strip()
            last_name = request.POST.get("last_name", "").strip()
            email = request.POST.get("email", "").strip()
            phone = request.POST.get("phone", "").strip()

            if not first_name or not last_name or not email or not phone:
                print("❌ Error: Missing user details")
                return redirect("bus_booking:index")

            # ✅ Assign User to Booking
            user = request.user if request.user.is_authenticated else None

            # ✅ If the user is logged in, assign previous bookings based on email
            if user:
                previous_bookings = Booking.objects.filter(email=email, user=None)
                for booking in previous_bookings:
                    booking.user = user
                    booking.save()

            # ✅ Calculate Total Price
            total_price = calculate_discounted_price(route, adults, children, students, retired)

            # ✅ Generate Unique Booking Reference
            booking_reference = generate_booking_reference()

            # ✅ Save Booking to Database
            booking = Booking.objects.create(
                user=user,  # Assign user if logged in
                route=route,
                passengers=total_passengers,
                total_price=total_price,
                booking_date=booking_date,
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
                booking_reference=booking_reference,
            )

            print(f"✅ Booking confirmed: {booking_reference} - {total_price:.2f} EUR - {total_passengers} passengers")

            # ✅ Determine Currency
            country = DESTINATION_COUNTRY_MAPPING.get(destination_name, "GERMANY")  # Default: Germany
            currency = CURRENCY_MAPPING.get(country, "EUR")  # Default: EUR

            # ✅ Send Confirmation Email
            subject = f"Booking Confirmation - {booking_reference}"
            message = f"""
            **Booking Confirmation**  

            **Booking Reference:** {booking_reference}  
            **Destination:** {destination_name}  
            **Date:** {booking_date.strftime('%d %B %Y')}  
            **Number of Passengers:** {total_passengers}  
            **Total Price:** {total_price:,.2f} {currency}  

            **Customer:** {first_name} {last_name}  
            **Contact:** {email} / {phone}  

            Thank you for choosing our bus service!  
            """

            send_mail(
                subject,
                message,
                "busstation@example.com",
                [email, "owner@example.com"],
                fail_silently=False,
            )

            # ✅ Redirect to Success Page
            return redirect("bus_booking:booking_success", reference=booking_reference)

        except Exception as e:
            import traceback
            print("❌ Exception Occurred:", e)
            traceback.print_exc()
            return redirect("bus_booking:index")

    return redirect("bus_booking:index")
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from bus_booking.models import Booking  # Import your Booking model
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Booking
def booking_history(request):
    bookings = None  # Default to None if no bookings found
    user_search = False  # Track if the user searched manually

    if request.user.is_authenticated:
        # ✅ Show only bookings for logged-in user
        bookings = Booking.objects.filter(user=request.user).order_by('-created_at')
    elif request.method == "POST":
        email = request.POST.get("email")
        phone = request.POST.get("phone")

        if email or phone:
            # ✅ Fetch bookings using email or phone number (for guests)
            bookings = Booking.objects.filter(email=email) if email else Booking.objects.filter(phone=phone)
            user_search = True  # Mark that a guest searched manually

    return render(request, 'bus_booking/booking_history.html', {
        'bookings': bookings,
        'user_search': user_search,  # Pass this to the template
    })

def booking_success(request, reference):
    # ✅ Fetch the booking using the real reference
    booking = get_object_or_404(Booking, booking_reference=reference)
    return render(request, "bus_booking/booking_success.html", {"booking": booking})


def about(request):
    return render(request, "about.html")



def contact(request):
    if request.method == "POST":
        email = request.POST.get("email")
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        # Send Email Notification (Optional)
        send_mail(
            subject=f"New Contact Form Submission from {name}",
            message=f"Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}",
            from_email=email,
            recipient_list=["aqdaszulfiqar30@gmail.com"],  # Change this to your email
        )

        messages.success(request, "Your message has been sent successfully!")
        return render(request, "contact.html")

    return render(request, "contact.html")


from django.contrib.auth.views import LogoutView
from django.shortcuts import redirect
from django.contrib.auth.views import LogoutView
from django.shortcuts import redirect

class CustomLogoutView(LogoutView):
    def get(self, request):
        return self.post(request)  # Treat GET as POST

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def custom_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect("bus_booking:index")  # Redirect after login
        else:
            messages.error(request, "Invalid username or password")

    return render(request, "login.html")



def checkout(request):
    return render(request, "bus_booking/checkout.html")

from django.utils.translation import get_language
from django.http import HttpResponse

def test_language(request):
    return HttpResponse(f"Current language: {get_language()}")
