# jobs/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('jobs/', views.job_listing_list, name='job_listing_list'),
    path('jobs/<int:pk>/', views.job_listing_detail, name='job_listing_detail'),
]

