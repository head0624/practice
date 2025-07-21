from . import views
from django.urls import path

urlpatterns=[
    path('',views.stats_view)
]