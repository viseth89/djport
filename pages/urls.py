from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('guysnbeermock/', views.guysnbeer, name='guysnbeermock'),
    path('experience', views.experience, name='experience')
]