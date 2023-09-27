from django.urls import path
from . import views

urlpatterns = [
    path('elector_keygen/', views.elector_keygen)
]
