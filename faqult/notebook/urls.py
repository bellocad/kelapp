from django.urls import path
from . import views

app_name = 'notebook'
urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('notebook/',views.NotebookList.as_view(),name='Notebook_list'),
    path('notebook/<int:pk>',views.NotebookDetailView.as_view(),name='NotebookDetail'),
    path('notebook/edit/<int:id>/', views.EditNotebook, name='EditNotebook'),
    path('post/', views.postview, name='post'),
]