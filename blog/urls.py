from django.urls import path
from . import views

urlpatterns = [
    path('', views.allBlogs, name='allBlogs'),
    path('about/', views.blogDetail, name='blogDetail'),
]