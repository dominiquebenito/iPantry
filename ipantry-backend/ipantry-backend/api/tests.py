"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

import django
from django.test import TestCase
from .models import (
    Ingredients,
    Recipes)

# TODO: Configure your database in settings.py and sync before running tests.
class IngredientsModelTestCase(TestCase):
    """This defines the test suite for the Ingredients model"""

    def setUp(self):
        """Define test client and other test variables"""
        self.ingredient_name = "all purpose flour"
        self.ingredient = Ingredients(name=self.ingredient_name)

    def test_model_can_create_ingredient(self):
        """Test the ingredient model can create an ingredient"""
        old_count = Ingredients.objects.count()
        self.ingredient.save()
        new_count = Ingredients.objects.count()
        self.assertNotEqual(old_count, new_count)