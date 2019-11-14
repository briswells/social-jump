from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.safestring import mark_safe
import json
# Create your views here.

def index(request):
    return render(request,'chat/index.html',{})

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