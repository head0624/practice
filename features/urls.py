from . import views
from django.urls import path

urlpatterns = [
    path('', views.features_view)
]