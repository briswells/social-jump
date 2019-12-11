

from django import forms
from django.core.validators import validate_slug
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

import datetime
from . import models

class UserRegistrationForm(UserCreationForm):

class postForm(forms.Form):
    post = forms.CharField(label='Post', max_length=240, validators=[validate_slug])
    image = forms.ImageField(label="Image File")
    image_description = forms.CharField(label='Image Description', max_length=240)

    def save(self, request, commit=True):
        new_sugg = models.Suggestion(
            message=self.cleaned_data["post"],
            image=self.cleaned_data["image"],
            image_description=self.cleaned_data["image_description"],
            author=request.user,
            date=datetime.datetime.now()
        )
        if commit:
            new_sugg.save()
        return new_sugg

# class CommentForm(forms.Form):
#     comment = forms.CharField(label='Comment', max_length=240, validators=[validate_slug])
#
#     def save(self, request, post_id, commit=True):
#         post_instance = models.userContent.objects.get(id=post_id)
#         new_comm = models.Comment(
#             post=post_instance,
#             comment=self.cleaned_data["comment"])
#         new_comm.author = request.user
#         if commit:
#             new_comm.save()
#         return new_comm

class RegistrationForm(UserCreationForm):

    email = forms.EmailField(
        label="Email",
        required=True
        )

    class Meta:
        model = User
        fields = ("username", "email",
                  "password1", "password2")

    def save(self, commit=True):

        user = super(UserRegistrationForm, self).save(commit=False)

        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class PersonalInfoForm(forms.Form):
    name = forms.CharField(label='Name', max_length=240)
