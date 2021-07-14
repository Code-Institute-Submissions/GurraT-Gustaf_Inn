from django.db import models

from django.conf import settings
from products.models import Product
from profiles.models import UserProfile


# Create your models here.

class Companyinfo(models.Model):
    title = models.CharField(max_length=68)
    news = models.TextField(max_length=564)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title
