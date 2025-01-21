from django.contrib import admin
from .models import Category, Event, Book, Profile

# Register your models here.

admin.site.register(Category)
admin.site.register(Event)
admin.site.register(Book)
admin.site.register(Profile)