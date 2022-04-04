from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass


class Lead(models.Model):
    ismi = models.CharField(max_length=20)
    familiyasi = models.CharField(max_length=20)
    yoshi = models.IntegerField(default=0)
    waiter = models.ForeignKey("Waiter", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.ismi)

class Waiter(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)