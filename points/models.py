from django.db import models
from recreation.models import Recreation
from comments_reviews.models import Reviews
from adress.models import Adress

class Points(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(default=None)
    approve = models.BooleanField(default=False)
    attractions = models.ManyToManyField(Recreation)
    comments = models.ManyToManyField(Reviews)
    adress = models.ForeignKey(Adress, on_delete=models.CASCADE, null=True, blank=True)


    def __self__(self):
        return self.nome
