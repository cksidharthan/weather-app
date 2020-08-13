from django.urls import path
from . import views

urlpatterns = [
    path('search-location/', views.get_search_data),
]