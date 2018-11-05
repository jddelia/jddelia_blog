from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=75)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    image = models.CharField(max_length=500)
    alt = models.CharField(max_length=100)
    tags = models.CharField(max_length=100)

    def __str__(self):
        return self.title
