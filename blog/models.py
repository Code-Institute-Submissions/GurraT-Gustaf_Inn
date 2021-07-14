from django.db import models

from django.conf import settings
from products.models import Product
from profiles.models import UserProfile

# Create your models here.

class Reviews(models.Model):
    productname = models.CharField(max_length=68)
    title = models.CharField(max_length=68)
    reviews = models.TextField(max_length=564)
    alias = models.CharField(max_length=68)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title

class CommentReviews(models.Model):
<<<<<<< HEAD
=======
    # not in use at the moment, could be used to add comments to reviews
>>>>>>> 02c3a0e493943218c9b52183ff524a90dd889041
    Title = models.OneToOneField(Reviews, on_delete=models.CASCADE, related_name="comment")
    date = models.DateTimeField(auto_now_add=True)
    comments = models.TextField(max_length=564)


    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.comments


