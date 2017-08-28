from django.conf.urls import url
from recipes.views import RecipeListView, RecipeDetailView


urlpatterns = [
    url(r'^$', RecipeListView.as_view()),
    url(r'^(?P<pk>\d+)/$', RecipeDetailView.as_view()),

]
