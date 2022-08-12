from django.shortcuts import render, HttpResponse, redirect
from .models import Categories, Dish, About, Specials, WhyUs, Events, Gallery, UserReservation
from .forms import UserReservationForm

# Create your views here.


def base(request):
    if request.method == 'POST':
        reservation = UserReservationForm(request.POST)
        if reservation.is_valid():
            reservation.save()
            return redirect('/')

    categories = Categories.objects.filter(is_visible=True)
    dishes = Dish.objects.filter(is_visible=True)
    specials = Dish.objects.filter(specialty=True)
    about_us = About.objects.all()
    spes_propositions = Specials.objects.filter(is_visible=True)
    descriptions = WhyUs.objects.all()[:1]
    descriptions2 = WhyUs.objects.all()[1:2]
    descriptions3 = WhyUs.objects.all()[2:3]
    event = Events.objects.all()[:1]
    event2 = Events.objects.all()[1:2]
    event3 = Events.objects.all()[2:3]
    gallery = Gallery.objects.all()
    reservation = UserReservationForm()

    data = {
        'categories': categories,
        'dishes': dishes,
        'specials': specials,
        'about_us': about_us,
        'spes_propositions': spes_propositions,
        'descriptions': descriptions,
        'descriptions2': descriptions2,
        'descriptions3': descriptions3,
        'event': event,
        'event2': event2,
        'event3': event3,
        'gallery': gallery,
        'reservation_form': reservation,
    }

    return render(request, 'base.html', context=data)