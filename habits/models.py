from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    pass

class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="habits")
    habit = models.CharField(max_length=64)
    description = models.CharField(max_length=255)
    status = models.CharField(max_length=64, default="Habit being formed")
    times_completed = models.IntegerField(default=0)
    private = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user} has a habit of {self.habit} and it is {self.status}"