from rest_framework import serializers
from .models import Movie, Seat, Booking

# Serializer for the Movie model
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__' # Include all fields: title, description, release date, duration

# Serializer for the Seat model
class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = '__all__' # Include all fields: seat number, booking status

# Serializer for the Booking model
class BookingSerializer(serializers.ModelSerializer):
    # To display the actual movie title and seat number instead of just IDs
    movie_title = serializers.ReadOnlyField(source='movie.title')
    seat_number = serializers.ReadOnlyField(source='seat.seat_number')

    class Meta:
        model = Booking
        fields = ['id', 'movie', 'seat', 'user', 'booking_date', 'movie_title', 'seat_number'] 
        read_only_fields = ['user', 'booking_date']
