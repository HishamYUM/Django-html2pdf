from django.urls import path
from . import views

urlpatterns = [
    path('quotation/', views.get),
]