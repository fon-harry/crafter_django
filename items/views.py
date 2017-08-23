from django.views.generic.list import ListView
from items.models import Item


class ItemListView(ListView):
    model = Item

