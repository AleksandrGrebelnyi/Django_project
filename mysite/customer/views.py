from django.shortcuts import render, HttpResponse

def customer(requesr, customer_num):
    return HttpResponse(f'Customer {customer_num}')

def customer_general(request):
    return HttpResponse('Base page of Customer')
