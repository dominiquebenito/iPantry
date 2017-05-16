from rest_framework import serializers
from .models import Ingredients, Recipes

class RecipeSerializer(serializers.ModelSerializer):
    """Serializer for Recipes Model"""

    class Meta:
        model = Recipes
        fields = ('id', 'name', 'steps', 'ingredients', 'date_created', 'date_modified');
        read_only_fields = ('date_created', 'date_modified')

class IngredientSerializer(serializers.ModelSerializer):
    """Serializer for Ingredients Model"""

    class Meta:
        model = Ingredients
        fields = ('id', 'name', 'date_created', 'date_modified');
        read_only_fields = ('date_created', 'date_modified')

