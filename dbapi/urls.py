from django.urls import path
from . import views

urlpatterns = [
    path('spends/', views.SpendsView.as_view()),
]