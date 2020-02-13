from django.db import models

# Create your models here.

class Recreation(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(default=None)
    opening_hours = models.TextField(default=None)
    minimum_age = models.IntegerField()

    def __str__(self):
        return self.name