from django.db import models

# Create your models here.
class Person(models.Model):
    Name = models.CharField()
    age = models.IntegerField()
    
    
    def __str__(self):
        return self.Name