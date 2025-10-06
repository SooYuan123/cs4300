# bookings/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, SeatViewSet, BookingViewSet, movie_list, book_seat, booking_history

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'seats', SeatViewSet)
router.register(r'bookings', BookingViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('api/', include(router.urls)),
    # Template URLs (The homepage must be defined here)
    path('', movie_list, name='movie_list'),                                      
    path('book/<int:movie_id>/', book_seat, name='book_seat'),                    
    path('history/', booking_history, name='booking_history'),

]
