from django.db import models
from django.contrib.auth.models import User


class userExpanded(models.Model): #Adds on to default user class
    username = models.ForeignKey(User, on_delete=models.CASCADE)#FK from pre built user class
    friends = models.ManyToManyField(User, related_name='friend')
    # groups = models.ManyToManyField(Publication)
    # roles = #some type
    gameSprite = models.ImageField(
        max_length=144,
        upload_to='uploads/%Y/%m/%d/')
    Darkmode = models.BooleanField()

class userContent(models.Model): #A social feed post
    username = models.ForeignKey(
        User, on_delete=models.CASCADE)#FK from pre built user class
    message = models.CharField(max_length=500)#
    image = models.ImageField(
        max_length=144,
        upload_to='uploads/%Y/%m/%d/')
    image_description = models.CharField(max_length=240)
    date = models.DateTimeField(auto_now_add=True)

class comments(models.Model):
    ID = models.ForeignKey(
        userContent, on_delete=models.CASCADE)#maybe just use Djangos pre built one, pk/fk
    comment = models.CharField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)#FK

class messageTread(models.Model):
    participants = models.ManyToManyField(
        User)  #people in thread dictionary, names to user ID
    threadName = models.CharField(max_length=100)

class message(models.Model):
    threadID = models.ForeignKey(
        messageTread, on_delete=models.CASCADE)#maybe just use Djangos pre built one, pk/fk
    message = models.CharField(max_length=1000)
    image = models.ImageField(
        max_length=144,
        upload_to='uploads/%Y/%m/%d/')
    image_description = models.CharField(max_length=240)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)#FK

class gameStats(models.Model):
    models.ForeignKey(User, on_delete=models.CASCADE)#FK from pre built user class
    time = models.DateTimeField(auto_now_add=True)
    score = models.IntegerField()
    timeJumped = models.IntegerField()
