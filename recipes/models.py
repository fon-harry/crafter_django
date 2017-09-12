from django.db import models
from items.models import Item


class Recipe(models.Model):
    name = models.CharField(max_length=200)
    item = models.OneToOneField(Item)
    level = models.IntegerField(default=0)
    type = models.CharField(max_length=200)
    mp_cost = models.IntegerField(default=0)
    success_rate = models.IntegerField(default=0)

    def __str__(self):
        return self.item.name

    def get_absolute_url(self):
        return '/recipes/%i/' % self.id  # TODO fix to reverse()


class RecipeProduction(models.Model):
    recipe = models.ForeignKey(Recipe)
    item = models.ForeignKey(Item)
    count = models.IntegerField(default=0)

    def __str__(self):
        return '%s (%i)' % (self.item.name, self.count)


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe)
    item = models.ForeignKey(Item)
    count = models.IntegerField(default=0)

    def __str__(self):
        return '%s (%i)' % (self.item.name, self.count)
