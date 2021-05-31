# Acá vamos a definir las rutas de la APP "blogs"
from django.urls import path     
from . import views
urlpatterns = [
    path('', views.root),
    path('blogs', views.index),
    path('blogs/new', views.new),
    path('blogs/create', views.create),
    path('blogs/json', views.send_json),
    path('blogs/<number>', views.show),
    path('blogs/<number>/edit', views.edit),
    path('blogs/<number>/delete', views.destroy),
]