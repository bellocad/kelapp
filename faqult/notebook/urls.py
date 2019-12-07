from django.urls import path
from . import views

app_name = 'notebook'
urlpatterns = [
#notebook
    path('',views.IndexView.as_view(),name='index'),
    path('notebook/',views.NotebookList.as_view(),name='Notebook_list'),
    path('notebook/<int:pk>',views.NotebookDetailView.as_view(),name='NotebookDetail'),
    path('notebook/edit/<int:id>/', views.EditNotebook, name='EditNotebook'),
    path('post/', views.postview, name='post'),

#catatan
    path('catatan/',views.CatatanList.as_view(),name='Catatan_list'),
    path('catatan/edit/<int:id>/', views.EditCatatan, name='EditCatatan'),
    path('catatan_baru/', views.catatanbaru, name='catatanbaru'),
]