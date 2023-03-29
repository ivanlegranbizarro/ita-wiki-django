from django.urls import path

from . import views

app_name = 'wiki'

urlpatterns = [
    path('categories/', views.CategoryListCreateAPIView.as_view(), name='categories'),
    path('categories/<int:category_id>/',
         views.CategoryRetrieveUpdateDestroyAPIView.as_view(), name='category'),
    path('temas/', views.TemaListCreateAPIView.as_view(), name='temas'),
    path('temas/<int:tema_id>/',
         views.TemaRetrieveUpdateDestroyAPIView.as_view(), name='tema'),
    path('wikis/', views.WikiListCreateAPIView.as_view(), name='wikis'),
    path('wikis/<int:wiki_id>/',
         views.WikiRetrieveUpdateDestroyAPIView.as_view(), name='wiki'),
]
