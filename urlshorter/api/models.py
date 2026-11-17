from django.db import models

# Create your models here.
class shorturls(models.Model):
    
    original_url = models.URLField(max_length=500)
    short_url = models.SlugField(unique=True,blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.short_url