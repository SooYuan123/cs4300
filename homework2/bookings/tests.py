from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from .models import Movie, Seat, Booking
from datetime import date, timedelta

# Unit Tests for Models
class ModelTestCase(TestCase):
    def setUp(self):
        self.movie = Movie.objects.create(
            title="Test Movie",
            description="A test description.",
            release_date=date.today(),
            duration=120
        )
        self.seat = Seat.objects.create(seat_number="A1", booking_status=False)
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.booking = Booking.objects.create(
            movie=self.movie,
            seat=self.seat,
            user=self.user
        )

    def test_movie_creation(self):
        self.assertEqual(self.movie.title, "Test Movie")
        self.assertEqual(self.movie.duration, 120)

    def test_seat_status_change(self):
        self.assertEqual(self.seat.booking_status, False)
        self.seat.booking_status = True
        self.seat.save()
        self.assertEqual(self.seat.booking_status, True)

    def test_booking_relates_correctly(self):
        self.assertEqual(self.booking.movie, self.movie)
        self.assertEqual(self.booking.seat, self.seat)
        self.assertEqual(self.booking.user, self.user)


# Integration Tests for API Endpoints
class APITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='apiuser', password='apipassword')
        self.movie = Movie.objects.create(
            title="API Movie",
            description="API test.",
            release_date=date.today(),
            duration=90
        )
        self.available_seat = Seat.objects.create(seat_number="C5", booking_status=False)
        self.booked_seat = Seat.objects.create(seat_number="C6", booking_status=True)
        
        # Define URLs using reverse lookup
        self.movies_url = reverse('movie-list')
        self.seats_url = reverse('seat-list')
        self.bookings_url = reverse('booking-list')
        
    def test_movie_list_get(self):
        # Test to ensure movies list returns a 200 status code and one movie
        response = self.client.get(self.movies_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_seat_list_only_available(self):
        # Test to ensure seats list only returns available seats (C5, not C6)
        response = self.client.get(self.seats_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['seat_number'], 'C5')

    def test_create_booking_endpoint(self):
        # Data for a new booking
        booking_data = {
            'movie': self.movie.id,
            'seat': self.available_seat.id,
            'user': self.user.id
        }
        
        # Test creating a booking
        response = self.client.post(self.bookings_url, booking_data, format='json')
        
        # Expect a 201 Created status code
        self.assertEqual(response.status_code, 201)
        # Check that the seat is now booked
        self.available_seat.refresh_from_db()
        # Check if the Booking record was created.
        self.assertEqual(Booking.objects.count(), 1)
