from django.db import models
from django .contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


class User(AbstractUser):
    email =models.CharField(max_length =50, unique=True)
    

