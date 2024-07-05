from django.db import models
from django.contrib.auth.models import User

class Log(models.Model):
    def __str__(self):
        return f'{self.owner.username} - {self.exercise.name} on {self.date}'
    
    date = models.DateField()
    duration = models.FloatField() 
    notes = models.TextField(blank=True)
    exercise = models.ForeignKey(
        'exercise.Exercise', 
        related_name='logs', 
        on_delete=models.CASCADE,
    )
    owner = models.ForeignKey(
        "jwt_auth.User", 
        related_name='logs', 
        on_delete=models.CASCADE
    )
    

 

