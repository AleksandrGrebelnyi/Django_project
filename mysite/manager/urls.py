from django.urls import path
from .views import manager_general, manager, manager_menu

urlpatterns = [
    path('', manager_general),
    path('menu/', manager_menu),
]