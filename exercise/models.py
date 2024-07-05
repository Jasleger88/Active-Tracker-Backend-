from django.db import models

 
class Exercise(models.Model):
    def __str__(self):
        return f'{self.name}'

    name = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    category = models.ForeignKey(
        'category.Category',
        related_name='exercise',
        on_delete=models.CASCADE
    )

    
