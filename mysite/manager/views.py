from django.shortcuts import render, HttpResponse, redirect
from base.models import UserReservation

# Create your views here
def reservations_list(request):
    reservation = UserReservation.objects.filter(is_processed=False)
    return render(request, 'reservations_list.html', context={
        'reservation': reservation,
    })

def update_reservation(request, pk):
    UserReservation.objects.filter(pk=pk).update(is_processed=True)
    return redirect('manager:reservations_list')
