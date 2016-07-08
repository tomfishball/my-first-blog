# Create your models here.
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    photo = models.URLField(blank=True)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    location = models.CharField(max_length=100, default='DEFAULT VALUE')
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title