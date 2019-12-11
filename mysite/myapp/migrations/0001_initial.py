# Generated by Django 2.2.5 on 2019-12-11 19:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='gameStats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('score', models.IntegerField()),
                ('timeJumped', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='userExpanded',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gameSprite', models.ImageField(default='test', max_length=144, upload_to='content/spites/%user')),
                ('Darkmode', models.BooleanField()),
                ('friends', models.ManyToManyField(related_name='friend', to=settings.AUTH_USER_MODEL)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='userContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.CharField(default='test', max_length=500)),
                ('image', models.ImageField(max_length=144, upload_to='content/images/%Y/%m/%d/')),
                ('image_description', models.CharField(max_length=240)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='messageTread',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('threadName', models.CharField(default='test', max_length=100)),
                ('participants', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(default='test', max_length=1000)),
                ('image', models.ImageField(default='test', max_length=144, upload_to='content/images/%Y/%m/%d/')),
                ('image_description', models.CharField(default='test', max_length=240)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('threadID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.messageTread')),
            ],
        ),
        migrations.CreateModel(
            name='comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(default='test', max_length=1000)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.userContent')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
