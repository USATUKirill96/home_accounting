from django.urls import path
from . import views

urlpatterns = [
    path('spends/', views.SpendsView.as_view()),
    path('users/', views.UsersView.as_view()),
    path('validate/', views.ValidateView.as_view()),
    path('incomes/', views.IncomesView.as_view()),
]