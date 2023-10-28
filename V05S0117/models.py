from django.db import models

# Create your models here.

class Switch(models.Model):
    status = models.BooleanField()
