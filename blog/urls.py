from django.urls import path

from . import views

urlpatterns = [
    path('', views.blogIndex, name='blogIndex'),
    path('<int:blog_id>/', views.blogDetail, name='blogDetail')
]