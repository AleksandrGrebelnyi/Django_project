from django.shortcuts import render, HttpResponse

def manager(requesr):
    return HttpResponse(f'Manager')

def manager_general(request):
    return HttpResponse('Base page of MANAGER')

def manager_menu(request):
    return HttpResponse('Manager access to MENU')

def manager_events(request):
    return HttpResponse('Manager access to EVENTS')

def manager_gallary(request):
    return HttpResponse('Manager access to GALLARY')

def book_a_table(request):
    return HttpResponse('Manager access to BOOK TABLE')