from django.shortcuts import render, redirect, get_object_or_404
from django import forms
from .models import Category, Event, Book
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin



class EventCreate(LoginRequiredMixin, CreateView):
    model = Event
    fields = ['name', 'location', 'time', 'date', 'description', 'price', 'image', 'categories']

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        form.fields['categories'] = forms.ModelMultipleChoiceField(
            queryset=Category.objects.all(),
            widget=forms.SelectMultiple, 
            required=True
        )
        return form

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
        


class EventUpdate(LoginRequiredMixin, UpdateView):
    model = Event
    fields = ['name', 'location', 'time', 'date', 'description', 'price', 'image', 'categories']


class EventDelete(LoginRequiredMixin, DeleteView):
    model = Event
    success_url = '/events/'

# ///////////////////////////////////////////


def home(request):
    return render(request, 'home.html')



def about(request):
    return render(request, 'about.html')


@login_required
def category(request):
    categories = Category.objects.all()
    return render(request, 'category.html', {'categories': categories})


@login_required
def event_index(request): 
    category_id = request.GET.get('category') 
    if category_id: 
        events = Event.objects.filter(categories__id=category_id) 
    else: 
        events = Event.objects.all() 
    return render(request, 'events/index.html', {'events': events})


@login_required 
def book_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.user.is_authenticated: 
        print(f'User: {request.user.username}, Event: {event.name}') 
        if request.user != event.user: 
            if not Book.objects.filter(user=request.user, event=event).exists():
                print('Creating new booking') 
                Book.objects.create(user=request.user, event=event) 
                return redirect('event_detail', event_id=event.id) 
            else: 
                print('Booking already exists') 
            return redirect('event_detail', event_id=event.id) 
        else: 
            print('User is the event owner') 
            return redirect('login')
    


@login_required
def cancel_booking(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    if request.user.is_authenticated:
        Book.objects.filter(user=request.user, event=event).delete()
        return redirect('event_detail', event_id=event.id)
    else:
        return redirect('login')


@login_required
def booked_events(request):
    booked_events = Book.objects.filter(user=request.user).select_related('event')
    return render(request, 'booked_events.html', {'booked_events': booked_events})


@login_required
def event_detail(request, event_id):

    event = Event.objects.filter(id=event_id).first()

    if event is None:
        return redirect('event_list')

    total_bookings = event.bookings.count()

    return render(request, 'events/event_detail.html', {
        'event': event,
        'total_bookings': total_bookings
    })


@login_required 
def my_events(request): 
    my_events = Event.objects.filter(user=request.user) 
    return render(request, 'my_events.html', {'my_events': my_events})

@login_required
def profile(request):
    return render(request, 'users/profile.html')

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid Signup- Please try again later.'

    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


