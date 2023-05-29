from django.shortcuts import render
from tethys_sdk.routing import controller


@controller
def home(request):
    """
    Controller for the app home page.
    """
    context = {}
    return render(request, 'hydrocompute/home.html', context)
