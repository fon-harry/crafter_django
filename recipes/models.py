from django.db import models
from items.models import Item


class Recipe(models.Model):
    name = models.CharField(max_length=200)
    item = models.ForeignKey(Item)
    level = models.IntegerField(default=0)
    type = models.CharField(max_length=200)
    mpCost = models.IntegerField(default=0)
    successRate = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '/recipes/%i/' % self.id
