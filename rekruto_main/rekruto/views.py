from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    """Request processing View"""
    if request.method == 'GET':
        name = request.GET.get('name')
        message = request.GET.get('message')

        return HttpResponse(f'Hello {name}! {message}!')
