from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

from .models import Greeting


# Create your views here.
def index(request):
    print(settings.SECRET_KEY)
    return render(request, "index.html")


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
