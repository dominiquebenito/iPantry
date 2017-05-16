
from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns

from .views import (
                IngredientCreateView, 
                IngredientDetailsView,
                RecipeCreateView,
                RecipeDetailsView)

urlpatterns = {
    url(r'ingredients/$', IngredientCreateView.as_view(), name="ingredient"), 
    url(r'ingredients/(?P<pk>[0-9]+)/$', IngredientDetailsView.as_view(), name="ingredient_detail"),
    url(r'recipes/$', RecipeCreateView.as_view(), name="recipe"),
    url(r'recipes/(?P<pk>[0-9]+)/$', RecipeDetailsView.as_view(), name="recipe_detail")
}

urlpatterns = format_suffix_patterns(urlpatterns)