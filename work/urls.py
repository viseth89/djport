from django.urls import path

from . import views

urlpatterns = [
    path('', views.workIndex, name='workIndex'),
    path('<int:work_id>/', views.workDetail, name='workDetail')
]