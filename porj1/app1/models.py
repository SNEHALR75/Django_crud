from django.db import models

# Create your models here.
class Food(models.Model):
    id = models.IntegerField(primary_key=True,auto_created=True)
    title = models.CharField(max_length=200)
    descriptions = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)