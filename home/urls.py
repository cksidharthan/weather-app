from django.urls import path
from . import views

urlpatterns = [
    path('api/search/', views.HomeSearchCreate.as_view()),
]
