from django.urls import path
from . import views


urlpatterns = [
    path('intro/', views.func),
    path('form/', views.get_name)
]
