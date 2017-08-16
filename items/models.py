from django.db import models


class Item(models.Model):
    item_id = models.IntegerField(default=0)
    item_type = models.CharField(max_length=200)
    item_name = models.CharField(max_length=200)

    def __str__(self):
        return self.item_name
