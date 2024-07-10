from django.db import models

class Exercise(models.Model):
    def __str__(self):
        return f'{self.name} - {self.category.name}'
    
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    category = models.ForeignKey(
        'category.Category',
        related_name='exercises',
        on_delete=models.CASCADE
    )

    
