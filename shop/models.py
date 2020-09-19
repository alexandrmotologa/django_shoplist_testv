from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Product(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField()
    date_published = models.DateField()
    date_add = models.DateTimeField(default=timezone.now)
    author_post = models.ForeignKey(User, on_delete=models.CASCADE)