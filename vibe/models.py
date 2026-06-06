from django.db import models

# Create your models here.
class Vibe(models.Model):
    mood=models.CharField(max_length=50)
    energy=models.IntegerField()
    time_of_day=models.IntegerField(max_length=50)
    recommendation=models.CharField(max_length=200)
    date=models.DateField()