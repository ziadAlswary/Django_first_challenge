from django.db import models

# Create your models here.

class Brand(models.Model):
    """
    Brand for makeup app
    """
    name = models.CharField(max_length=50)
    orgin = models.TextField()
    
    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url():
        pass