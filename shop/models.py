from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Product(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField()
    date_published = models.DateField()
    date_add = models.DateTimeField(default=timezone.now)
    author_post = models.ForeignKey(User, on_delete=models.CASCADE)
    cover = models.ImageField(default='cover.png', upload_to='cover')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'pk': self.pk})
