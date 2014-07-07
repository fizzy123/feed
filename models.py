from django.db import models
from django.contrib.auth.models import User

class Source(models.Model):
    owner = models.ForeignKey(User)
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=200, primary_key=True)
    updated = models.DateTimeField(auto_now=True)

class Item(models.Model):
    source = models.ForeignKey(Source)
    url = models.CharField(max_length=200, primary_key=True)
    skipped = models.IntegerField(default=0)
    last_read = models.BooleanField(default=False)

