from django.urls import path

from csv_processing_api import views

urlpatterns = [
    path('csv/', views.CsvProcessingView.as_view())
]