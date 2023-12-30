from django.contrib.auth.models import User
from django.db import models


class Adv(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    open = models.BooleanField(default=True)
    text = models.TextField()
