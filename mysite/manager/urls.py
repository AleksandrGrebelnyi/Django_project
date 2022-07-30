from django.urls import path
from .views import manager_general, manager, manager_menu, manager_events, manager_gallary, book_a_table

urlpatterns = [
    path('', manager_general),
    path('menu/', manager_menu),
    path('events/', manager_events),
    path('gallary/', manager_gallary),
    path('book-a-table/',  book_a_table),
]