from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_search, name="home-page"),
    path('dashboard/', views.dashboard, name="dashboard"),
]