from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('project_create/', views.project_create, name='pr'),
    path('registration/', views.Registration.as_view()),
    path('project/<int:id>/', views.project),
    path('edit_project/<int:pk>/', views.ProjectEditPage.as_view()),
    path('text/', views.TestPage.as_view())
]
