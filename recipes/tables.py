import django_tables2 as tables
from recipes.models import Recipe


class RecipeTable(tables.Table):
    item = tables.LinkColumn()

    class Meta:
        model = Recipe
        exclude = ('name', 'type', 'mpCost', 'successRate',)
        attrs = {'class': 'paleblue'}