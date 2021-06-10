from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('shows', views.allShows),
    path('shows/new', views.addNewShow),
    path('shows/create', views.createNewShow),
    path('shows/<int:id>/', views.tvShow),
    path('shows/<int:id>/edit', views.editShow),
    path('shows/<int:id>/update', views.updateShow),
    path('shows/<int:id>/destroy', views.deleteShow)
]