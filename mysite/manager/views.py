from django.shortcuts import render, HttpResponse

def manager(requesr):
    return HttpResponse(f'Manager')

def manager_general(request):
    return HttpResponse('Base page of Manager')

def manager_menu(request):
    return HttpResponse('Manager access to menu')