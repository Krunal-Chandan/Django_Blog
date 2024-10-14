from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    datePosted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk})


class TestModel(models.Model):
    title = models.CharField(max_length=64, help_text="Please input model title.")
    published = models.BooleanField(verbose_name="Is this test model published.")
    is_demo = models.BooleanField(help_text="Is this a demo test model?")