import django_tables2 as tables
from recipes.models import Recipe


class RecipeTable(tables.Table):
    item = tables.LinkColumn()

    class Meta:
        model = Recipe
        attrs = {'class': 'paleblue'}