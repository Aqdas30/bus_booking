from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView  # Add this import

from django.contrib.auth.views import LogoutView
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views  # Import views
app_name = "bus_booking"

urlpatterns = [
    path('', views.index, name='index'),  # Home page view

    path('book/', views.book_ticket, name='book_ticket'),
    path('booking-history/', views.booking_history, name='booking_history'),
    path('booking-success/<str:reference>/', views.booking_success, name='booking_success'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),   
    path("gallery/", views.gallery, name="gallery"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path('checkout/', views.checkout, name='checkout'),  # NEW CHECKOUT PAGE
    path('test-lang/', views.test_language),



    # ✅ Ensure logout redirects to 'index' (home page)
    path('logout/', auth_views.LogoutView.as_view(next_page='bus_booking:index'), name='logout'),
]
