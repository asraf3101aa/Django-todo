from django.db import models

# Create your models here.
class Todo(models.Model): 
    task = models.CharField(max_length=100)
    date = models.DateField()
    is_complete = models.BooleanField(default=False)
    description = models.TextField()
    