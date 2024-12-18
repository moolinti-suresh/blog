from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse


# Create your models here.

class Post(models.Model):
    title   =   models.CharField(max_length = 255)
    content =   models.TextField(max_length = 1000)
    date_posted = models.DateTimeField(auto_now_add = True)
    author  = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.id})
