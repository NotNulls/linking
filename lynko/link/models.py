from django.db import models

from accounts.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=225)
    created_by = models.ForeignKey(User, related_name='categories', on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)


class Link(models.Model):
    category = models.ForeignKey(Category, related_name='links', on_delete=models.CASCADE)
    name = models.CharField(max_length=225)
    description = models.TextField(blank=True, null=True)
    url = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, related_name='links', on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)

