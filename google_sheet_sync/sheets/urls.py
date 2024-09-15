from django.urls import path
from . import views

urlpatterns = [
    path('sheets/', views.google_sheets_example, name='google_sheets_example'),
]
