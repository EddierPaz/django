from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('crear/', views.crear_hojita, name='crear_hojita'),
    path('editar/<int:id>/', views.editar_hojita, name='editar_hojita'),
    path('eliminar/<int:id>/', views.eliminar_hojitas, name='eliminar_hojita'),
]