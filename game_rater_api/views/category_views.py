from dataclasses import field, fields
from telnetlib import STATUS
from django import http
from rest_framework.viewsets import ViewSet
from game_rater_api.models import Category
from rest_framework import serializers
from rest_framework.serializers import ValidationError
from rest_framework.response import Response
from django.http import HttpResponseServerError
from game_rater_api.models.reviewer import Reviewer


from logging import raiseExceptions
from django.http import HttpResponseServerError
from rest_framework import serializers, status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model= Category
        fields= ("id", "name")
    



class CategoryView(ViewSet):
    
    def list(self, request):
        
        categories = Category.objects.all()
        
        serializer = CategorySerializer(categories, many= True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)