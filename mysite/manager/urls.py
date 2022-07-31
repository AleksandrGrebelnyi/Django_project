from django.urls import path
from .views import manager_general, addrecord, manager_menu, add_event, book_a_table, manager_events, delete_event, \
    cancel_book_table, add_dish, delete_dish

urlpatterns = [
    path('', manager_general),
    path('menu/', manager_menu),
    path('menu/add-dish', add_dish, name='add-dish'),
    path('menu/delete-dish/<str:dish_name>', delete_dish, name='delete-dish'),
    path('events/', manager_events),
    path('events/add-event/', add_event, name='add-event'),
    path('events/add-event/addrecord', addrecord, name='addrecord'),
    path('events/delete-event/<str:event_name>', delete_event, name='delete-event'),
    path('book-a-table/',  book_a_table),
    path('book-a-table/cancel',  cancel_book_table, name='cancel'),
]