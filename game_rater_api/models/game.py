from django.db import models

class Game(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    designer = models.CharField(max_length=50)
    year_released = models.IntegerField()
    number_of_players = models.IntegerField()
    estimated_time_to_play = models.IntegerField()
    age_recommendation = models.IntegerField()
    first_reviewer = models.ForeignKey("Reviewer", on_delete=models.CASCADE)
    categories = models.ManyToManyField("Category", related_name="games")
    
    
    @property
    def editable(self):
        return self.__editable
    @editable.setter
    def editable(self, value):
        self.__editable = value
    
    