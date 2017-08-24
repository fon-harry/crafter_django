from django.views.generic import ListView, DetailView
from items.models import Item


class ItemListView(ListView):
    model = Item


class ItemDetailView(DetailView):
    model = Item
