from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User




class Category(models.Model):
    TYPE_CHOICES = [
        ('indoor', 'indoor'),
        ('outdoor', 'outdoor'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='main_app/static/uploads/', default="")
    type = models.CharField(max_length=20, choices=TYPE_CHOICES , default="indoor")
    
    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id': self.id})

    def __str__(self):
        return f"Category Type: {self.get_type_display()}"


class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey('Event', on_delete=models.CASCADE, related_name='bookings')
    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking by {self.user.username} for {self.event.name}"



class Event(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    time = models.CharField(max_length=10)
    date = models.DateField()
    description = models.TextField(max_length=250)
    price = models.IntegerField()
    image = models.ImageField(upload_to='main_app/static/uploads/', default="")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, related_name='events')

    def get_absolute_url(self):
        return reverse('event_detail', kwargs={'event_id': self.pk})

    def total_bookings(self):
        return self.bookings.count()

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField()

    def __str__(self):
        return self.user.username
