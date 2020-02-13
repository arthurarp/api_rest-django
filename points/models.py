from django.db import models

class Points(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(default=None)
    approve = models.BooleanField(default=False)


    def __self__(self):
        return self.nome
