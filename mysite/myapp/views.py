from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
import json

from . import models
from . import forms

# Create your views here.

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

def index(request, page=0):
    if request.method == "POST":
        if request.user.is_authenticated:
            form_instance = forms.postForm(request.POST)
            if form_instance.is_valid():
                new_sugg = models.userContent(post=form_instance.cleaned_data["post"])
                new_sugg.username = request.user
                new_sugg.save()
                form_instance = forms.postForm()
        else:
            form_instance = forms.postForm()
    else:
        form_instance = forms.postForm()
    posts = models.userContent.objects.all()
    # content_list = {"posts":[]}
    # for p_q in post_query:
        # comment_query = models.Comment.objects.filter(ID=p_q)
        # comment_list = []
        # for c_q in comment_query:
        #     can_delete=False
        #     if request.user == c_q.author:
        #         can_delete=True
        #     comment_list += [{
        #     "comment":c_q.comment,
        #     "author":c_q.author.username,
        #     "created_on":c_q.date,
        #     "id":c_q.ID,
        #     "delete":can_delete
        #     }]
        # content_list["post"] += [{
        #     "id":p_q.id,
        #     "post":p_q.post,
        #     "author":p_q.username.username,
        #     "created_on":p_q.date
        #     # "comments":comment_list
        #     }]
    context = {
        "variable":"Hello World",
        "title":"Index",
        "form":form_instance,
        "post_list":posts
    }
    return render(request, "base.html", context=context)

@csrf_exempt
@login_required(login_url='/login/')
def contents_view(request):
    if request.method == "GET":
        suggestion_query = models.userContent.objects.all().order_by('-created_on')
        suggestion_list = {"userContent":[]}
        # for s_q in suggestion_query:
        #     comment_query = models.Comment.objects.filter(suggestion=s_q)
        #     comment_list = []
        #     for c_q in comment_query:
        #         can_delete=False
        #         if request.user == c_q.username:
        #             can_delete=True
        #         comment_list += [{
        #         "comment":c_q.comment,
        #         "author":c_q.username.username,
        #         "created_on":c_q.date,
        #         "id":c_q.id,
        #         "delete":can_delete
        #         }]
        #     url = ""
        #     if not str(c_q.image)=="":
        #         url=c_q.image.url
        #     suggestion_list["suggestions"] += [{
        #         "id":c_q.id,
        #         "post":c_q.post,
        #         "author":c_q.username.username,
        #         "created_on":c_q.date,
        #         "comments":comment_list,
        #         "image":url,
        #         "image_description":c_q.image_description
        #         }]
        return JsonResponse(suggestion_list)
    return HttpResponse("Unsupported HTTP Method")

@login_required(login_url='/login/')
def suggestion_form_view(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            form_instance = forms.postForm(request.POST, request.FILES)
            if form_instance.is_valid():
                new_sugge = form_instance.save(request=request)
                return redirect("/")
        else:
            return redirect("/")
    else:
        form_instance = forms.postForm()
    context = {
        "title":"Post Form",
        "form":form_instance
    }
    return render(request, "post.html", context=context)

def test(request):
    context={
        "title":"Index",
        "var":"YAY imma god",
        "some_list":range(20)

    }
    return render(request, "base.html", context = context)

def game(request):
    return render(request, "game.html")
