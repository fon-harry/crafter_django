from django.views.generic import ListView, DetailView
from recipes.models import Recipe
from django_tables2 import SingleTableView
from recipes.tables import RecipeTable


class RecipeListView(SingleTableView):
    model = Recipe
    table_class = RecipeTable


class RecipeDetailView(DetailView):
    model = Recipe
