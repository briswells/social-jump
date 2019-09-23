from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("CINS465 Hello World")

def test(request):
    context={
        "title":"Index",
        "var":"YAY imma god",
        "some_list":range(20)

    }
    return render(request, "base.html", context = context)
