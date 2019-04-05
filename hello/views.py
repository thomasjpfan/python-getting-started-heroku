from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting


# Create your views here.
def index(request):
    import os
    print(os.environ['SECRET_KEY'])
    return render(request, "index.html")


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
