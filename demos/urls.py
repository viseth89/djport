from django.urls import path

from . import views

urlpatterns = [
    path('bootstrap4a',views.bootstrap4a, name='bootstrap4a')
]