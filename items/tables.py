import django_tables2 as tables
from items.models import Item


class ItemTable(tables.Table):
    name = tables.LinkColumn()

    class Meta:
        model = Item
        attrs = {'class': 'paleblue'}