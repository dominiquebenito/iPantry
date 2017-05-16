from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .serializers import IngredientSerializer, RecipeSerializer
from .models import Ingredients, Recipes


#
#   Ingredient Views and Endpoints
#

class IngredientCreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Ingredients.objects.all()
    serializer_class = IngredientSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new ingredient."""
        serializer.save()

class IngredientDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles single GET, PUT and DELETE requests for Ingredients"""
    queryset = Ingredients.objects.all()
    serializer_class = IngredientSerializer


#
#   Recipe Views and Endpoints
#
class RecipeCreateView(generics.ListCreateAPIView):
    """This class defined the behavior of the view for the Recipes"""
    queryset = Recipes.objects.all()
    serializer_class = RecipeSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new recipe."""
        serializer.save()

class RecipeDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles single GET, PUT and DELETE requests for Ingredients"""
    queryset = Recipes.objects.all()
    serializer_class = RecipeSerializer