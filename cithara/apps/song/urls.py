from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('create/', views.CreateView.as_view(), name="create"),
    path('create/create_song/', views.create_song, name="create_song"),
    path('update/<int:pk>/', views.UpdateView.as_view(), name="update"),
    path('update/update_song/<int:id>/', views.update_song, name="update_song"),
    path('delete/<int:id>/', views.delete, name="delete"),
]