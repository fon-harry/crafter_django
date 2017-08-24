from django.db import models


class Item(models.Model):
    type = models.CharField(max_length=200)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '/items/%i/' % self.id
