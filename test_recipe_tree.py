import os
import django
os.environ['DJANGO_SETTINGS_MODULE'] = 'crafter.settings'
django.setup()
from recipes.models import Recipe, RecipeProduction, RecipeIngredient
from collections import Counter

def main():
    # recipe = Recipe.objects.get(pk=644)
    #
    # for ingredient in recipe.recipeingredient_set.all():
    #     ingredient_recipe = RecipeProduction.objects.filter(item=ingredient.item)
    #     print(ingredient, ingredient_recipe.count())
    #     # if ingredient_recipe.count() > 0:
    #     #     print(ingredient_recipe)

    counter = Counter(RecipeProduction.objects.all())

    print(type(counter))

    for item, i in counter:
        print(item)


if __name__ == '__main__':
    main()
