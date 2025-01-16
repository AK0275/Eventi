from django.db import models
from django.urls import reverse

# Create your models here.

Social = 'Social'
Sports = 'Sports'
Foods = 'Foods'
Festivals = 'Festivals'
Outdoor = 'Outdoor'
Other = 'Other'


EVENT_TYPE = [
        (Social, 'Social'),
        (Sports, 'Sports'),
        (Foods, 'Foods'),
        (Festivals, 'Festivals'),
        (Outdoor, 'Outdoor'),
        (Other, 'Other'),
    ]

class category(models.Model):
    type = models.CharField(max_length=100, choices=EVENT_TYPE, default=Social,)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'category_id': self.id})


    def __str__(self):
        return self.type


