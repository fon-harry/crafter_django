from django.views.generic import ListView, DetailView
from recipes.models import Recipe


class RecipeListView(ListView):
    model = Recipe


class RecipeDetailView(DetailView):
    model = Recipe
