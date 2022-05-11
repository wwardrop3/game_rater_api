from django.db import models

class Review(models.Model):
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    reviewer = models.ForeignKey("Reviewer", on_delete=models.CASCADE)
    review_text = models.CharField(max_length=400)
    rating = models.DecimalField(max_digits=4, decimal_places=1)
    