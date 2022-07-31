from django.shortcuts import render, HttpResponse

def manager(requesr):
    return HttpResponse(f'Manager')

def manager_general(request):
    return HttpResponse('Base page of MANAGER')

def manager_menu(request):
    return HttpResponse('Manager access to MENU')

def add_dish(request):
    return HttpResponse('Manager access to ADD-DISH-TO-MENU')

def delete_dish(request):
    return HttpResponse('Manager access to DELETE-DISH')

def manager_events(request):
    return HttpResponse('Manager access to manager_events')

def add_event(request):
    return HttpResponse('Manager access to ADD-EVENTS')

def addrecord(request):
    return HttpResponse('Manager access to ADD-RECORD')

def delete_event(request, event_name):
    return HttpResponse('Manager access to DELETE_EVENT')

def book_a_table(request):
    return HttpResponse('Manager access to BOOK TABLE')

def cancel_book_table(request):
    return HttpResponse('Manager access to CANCEL-BOOK')

