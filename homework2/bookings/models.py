
# bookings/models.py

from django.db import models
from django.contrib.auth.models import User # Django's built-in User model

# Title, description, release date, and duration of the movie
class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    release_date = models.DateField()
    duration = models.IntegerField(help_text="Duration in minutes")
    
    def __str__(self):
        return self.title

# Seat number and availability
class Seat(models.Model):
    seat_number = models.CharField(max_length=10, unique=True)
    # Using a Boolean to indicate if the seat is currently booked
    booking_status = models.BooleanField(default=False) 

    def __str__(self):
        return self.seat_number

# Movie, seat, user, and date of the booking
class Booking(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking for {self.movie.title} by {self.user.username}"
