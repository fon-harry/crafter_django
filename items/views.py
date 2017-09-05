from django.views.generic import DetailView
from items.models import Item
from django_tables2 import SingleTableView
from items.tables import ItemTable


class ItemListView(SingleTableView):
    model = Item
    table_class = ItemTable


class ItemDetailView(DetailView):
    model = Item
