from django.urls import path

from . import views

urlpatterns = [
    path('bootstrap4a', views.bootstrap4a, name='bootstrap4a'),
    path('bootstrap4b', views.bootstrap4b, name='bootstrap4b'),
    path('bootstrap4c', views.bootstrap4c, name='bootstrap4c')
]