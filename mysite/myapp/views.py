from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.safestring import mark_safe
import json

from . import forms
from . import models
# Create your views here.

def index(request):
    return render(request,'home.html',{})

def test(request):
    context={
        "title":"Index",
        "var":"YAY imma god",
        "some_list":range(20)

    }
    return render(request, "base.html", context = context)

def room(request,room_name):
    return render(request,'chat/room.html',{
        'room_name_json': mark_safe(json.dumps(room_name))
    })


def register(request):
    if request.method == 'POST':
        form = forms.UserRegistrationForm(request.POST)
        if form.is_valid():
           form.save()
           return redirect("/login/")
    else:
        form = forms.UserRegistrationForm()
    context = {
        "form":form,
    }
    return render(request,'registration/register.html',context=context)


def logout_view(request):
    logout(request)
    return redirect("/login/")