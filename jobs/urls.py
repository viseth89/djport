from django.urls import path

from . import views

urlpatterns = [
    path('', views.jobIndex, name='jobIndex'),
    path('<int:job_id>/', views.jobDetail, name='jobDetail')
]