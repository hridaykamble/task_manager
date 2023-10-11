
# Create your models here.
from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(
        max_length=10,
        choices=[('Pending', 'Pending'), ('Completed', 'Completed')],
        default='Pending'
    )

    def __str__(self):
        return self.title
