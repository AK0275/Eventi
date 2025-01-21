from django.urls import path
from . import views
from .views import profile



urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('category/', views.category, name='category'),
    path('events/', views.event_index, name='event_index'),
    path('events/<int:event_id>/', views.event_detail, name='event_detail'),

    path('events/create/', views.EventCreate.as_view(), name='events_create'),
    path('events/<int:event_id>/book' , views.book_event, name="book_event"),
    path('events/<int:event_id>/cancel/', views.cancel_booking, name='cancel_booking'),

    path('booked-events/', views.booked_events, name='booked_events'),
    path('my-events/', views.my_events, name='my_events'),

    path('events/<int:pk>/update/', views.EventUpdate.as_view(), name='events_update'),
    path('events/<int:pk>/delete/', views.EventDelete.as_view(), name='event_delete'),

    path('accounts/signup/', views.signup, name='signup'),

    path('profile/', profile, name='users-profile'),
]
