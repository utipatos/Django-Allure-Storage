from django.urls import path
from app import views

urlpatterns = [
    path('result/', views.ResultListView.as_view()),
    path('report/', views.ReportListView.as_view()),
]
