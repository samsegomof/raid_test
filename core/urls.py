from django.urls import path
from core import views

urlpatterns = [
    path('frameworks/', views.FrameworkListView.as_view()),
    path('frameworks/<str:language>/', views.FrameworkDetailView.as_view()),
]
