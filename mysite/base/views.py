from django.shortcuts import render, HttpResponse

def base(request):
    return HttpResponse('Base')
