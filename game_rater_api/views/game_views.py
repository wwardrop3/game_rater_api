from dataclasses import field, fields
from telnetlib import STATUS
from django import http
from rest_framework.viewsets import ViewSet
from game_rater_api.models import Game
from rest_framework import serializers
from rest_framework.serializers import ValidationError
from rest_framework.response import Response
from django.http import HttpResponseServerError
from game_rater_api.models.category import Category
from game_rater_api.models.reviewer import Reviewer


from logging import raiseExceptions
from django.http import HttpResponseServerError
from rest_framework import serializers, status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        # the cate
        fields = ("id", "title", "description", "designer", "year_released", "number_of_players", "estimated_time_to_play", "age_recommendation", "first_reviewer", "categories", "editable")
        depth = 1
    



class GameView(ViewSet):
    
    def list(self, request):
        
        games = Game.objects.all()
        first_reviewer = Reviewer.objects.get(user = request.auth.user)
        
        for game in games:
            game.editable = request.auth.user == game.first_reviewer.user
        
        serializer = GameSerializer(games, many=True)
        
        return Response(serializer.data)
        
    
    def retrieve(self, request, pk):
        
        game = Game.objects.get(pk = pk)
        
        
        serializer = GameSerializer(game)
        
        return Response(serializer.data)
        
    
    def create(self, request):
        
        reviewer = Reviewer.objects.get(user = request.auth.user)
        
        game = Game.objects.create(
            
            title = request.data['title'],
            description = request.data['description'],
            designer = request.data['designer'],
            year_released= request.data['yearReleased'],
            number_of_players = request.data['numberOfPlayers'],
            estimated_time_to_play = request.data['estimatedTimeToPlay'],
            age_recommendation = request.data['ageRecommendation'],
            first_reviewer = reviewer
            )
        
        serializer = GameSerializer(game)
        
        return Response(None, status=status.HTTP_204_NO_CONTENT)


