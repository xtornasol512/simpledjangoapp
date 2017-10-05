''' Custom error pages '''
from django.shortcuts import render


def bad_request(request):
    return render(requests, "400.html")

def permission_denied(request):
    return render(requests, "403.html")


def page_not_found(request):
    return render(requests, "404.html")

def server_error(request):
    return render(requests, "500.html")
