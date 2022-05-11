from turtle import ondrag
from django.db import models

class Image(models.Model):
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    reviewer = models.ForeignKey("Reviewer", on_delete=models.CASCADE)
    image_url = models.CharField(max_length=100)
    
    