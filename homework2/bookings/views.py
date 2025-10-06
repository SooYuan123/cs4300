from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.permissions import AllowAny # Use the AllowAny permission for simplicity
from .models import Movie, Seat, Booking
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer

# Movie ViewSet: For CRUD operations on movies
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [AllowAny]

# Seat ViewSet: For seat availability and booking
class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer
    permission_classes = [AllowAny]

# Booking ViewSet: For users to book seats and view their booking history
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [AllowAny]


# Movie List View (for movie_list.html)
def movie_list(request):
    movies = Movie.objects.all()
    context = {'movies': movies}
    return render(request, 'bookings/movie_list.html', context)

# Seat Booking View (for seat_booking.html)
def book_seat(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    # Filter for available seats only 
    available_seats = Seat.objects.filter(booking_status=False) 

    if request.method == 'POST':
        seat_id = request.POST.get('seat_id')
        seat = get_object_or_404(Seat, pk=seat_id, booking_status=False)

        user = User.objects.first() 
        if not user:
             return redirect('movie_list')

        # Create the booking
        Booking.objects.create(movie=movie, seat=seat, user=user)
        # Update seat status
        seat.booking_status = True
        seat.save()

        return redirect('booking_history') # Redirect to history after successful booking

    context = {
        'movie': movie,
        'available_seats': available_seats
    }
    return render(request, 'bookings/seat_booking.html', context)

# Booking History View (for booking_history.html)
def booking_history(request): 
    user = User.objects.first() 

    if user:
        # Get all bookings for that user
        bookings = Booking.objects.filter(user=user).select_related('movie', 'seat').order_by('-booking_date')
    else:
        bookings = []

    context = {'bookings': bookings}
    return render(request, 'bookings/booking_history.html', context)
