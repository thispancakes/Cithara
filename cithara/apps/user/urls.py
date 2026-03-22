from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('create/', views.show_create, name="create"),
    path('create_user/', views.create_user, name="create_user"),
    path('update/<int:id>/', views.show_update, name="update"),
    path('update/update_user/<int:id>/', views.update_user, name="update_user"),
    path('delete/<int:id>/', views.delete, name="delete"),
]