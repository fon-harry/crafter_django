from django.conf.urls import url
from items.views import ItemListView, ItemDetailView


urlpatterns = [
    url(r'^$', ItemListView.as_view()),
    url(r'^(?P<pk>\d+)/$', ItemDetailView.as_view()),

]
