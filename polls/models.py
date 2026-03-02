from django.db import models

class Question(models.Model):
    Question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    

class Choice(models.Model):
    Question_text = models.ForeignKey(Question, on_delete=models.CASCADE)
    Choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

from django.db import models


class Question(models.Model):
    # ... 
    def __str__(self):
        return self.Question_text


class Choice(models.Model):
    # ...
    def __str__(self):
        return self.Choice_text

import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    # ...
    def __str__(self):
        return self.Question_text

def was_published_recently(self):
    now = timezone.now()
    return now - datetime.timedelta(days=1) <= self.pub_date <= now


from django.contrib import admin


class Question(models.Model):
    # ...
    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


