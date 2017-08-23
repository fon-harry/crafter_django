from django.conf.urls import url
from items.views import ItemListView


urlpatterns = [
    url(r'^$', ItemListView.as_view()),

]
