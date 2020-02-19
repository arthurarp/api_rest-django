from django.contrib.auth.models import User
from django.db import models

class Reviews(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    approve = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username