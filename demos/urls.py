from django.urls import path

from . import views

urlpatterns = [
    path('bootstrap4a', views.bootstrap4a, name='bootstrap4a'),
    path('bootstrap4b', views.bootstrap4b, name='bootstrap4b'),
    path('bootstrap4c', views.bootstrap4c, name='bootstrap4c'),
    path('bootstrap4d', views.bootstrap4d, name='bootstrap4d'),
    path('bootstrap4d/about', views.bootstrap4dAbout, name='bootstrap4dAbout'),
    path('bootstrap4d/blog', views.bootstrap4dBlog, name='bootstrap4dBlog'),
    path('bootstrap4d/contact', views.bootstrap4dContact, name='bootstrap4dContact'),
    path('bootstrap4d/services', views.bootstrap4dServices, name='bootstrap4dServices'),
    path('bootstrap4e', views.bootstrap4e, name='bootstrap4e'),
    path('jsjq1',views.jsjq1,name='jsjq1'),
]