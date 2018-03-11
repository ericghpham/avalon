from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import AbstractUser


class AvalonUser(AbstractUser):
    def __repr__(self):
        return self.username

class AvalonUserCreationForm(UserCreationForm):
    class Meta:
        model = AvalonUser
        fields = ("username",)