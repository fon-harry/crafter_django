from django.db import models
from items.models import Item


class Recipe(models.Model):
    name = models.CharField(max_length=200)
    item = models.OneToOneField(Item)
    level = models.IntegerField(default=0)
    type = models.CharField(max_length=200)
    mpCost = models.IntegerField(default=0)
    successRate = models.IntegerField(default=0)

    def __str__(self):
        return self.item.name

    def get_absolute_url(self):
        return '/recipes/%i/' % self.id


class RecipeProduction(models.Model):
    recipe = models.ForeignKey(Recipe)
    item = models.ForeignKey(Item)
    count = models.IntegerField(default=0)


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe)
    item = models.ForeignKey(Item)
    count = models.IntegerField(default=0)
