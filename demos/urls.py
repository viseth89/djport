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

    path('bootstrap4f', views.bootstrap4f, name='bootstrap4f'),
    path('bootstrap4f/categories', views.bootstrap4fCategories, name='bootstrap4fCategories'),
    path('bootstrap4f/details', views.bootstrap4fDetails, name='bootstrap4fDetails'),
    path('bootstrap4f/login', views.bootstrap4fLogin, name='bootstrap4fLogin'),
    path('bootstrap4f/posts', views.bootstrap4fPosts, name='bootstrap4fPosts'),
    path('bootstrap4f/profile', views.bootstrap4fProfile, name='bootstrap4fProfile'),
    path('bootstrap4f/settings', views.bootstrap4fSettings, name='bootstrap4fSettings'),
    path('bootstrap4f/users', views.bootstrap4fUsers, name='bootstrap4fUsers'),

    path('bootstrap4g', views.bootstrap4g, name='bootstrap4g'),
    path('bootstrap4g/products', views.bootstrap4gProducts, name='bootstrap4gProducts'),
    path('bootstrap4g/singleproduct', views.bootstrap4gSingleProduct, name='bootstrap4gSingleProduct'),
    path('bootstrap4g/store', views.bootstrap4gStore, name='bootstrap4gStore'),
    path('jsjq1/settings',views.jsjq1,name='jsjq1'),

    path('bootstrap4morning', views.bootstrap4morning, name='bootstrap4morning'),

    path('jpbootstrap2', views.jpbootstrap2, name='jpbootstrap2'),
    path('jpbootstrap3', views.jpbootstrap3, name='jpbootstrap3'),

    path('ccbootstrap4', views.ccbootstrap4, name='ccbootstrap4'),

    path('sassDemo', views.sassDemo, name='sassDemo'),
]