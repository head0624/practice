from . import views
from django.urls import path

app_name = 'concat'
urlpatterns=[
    path('', views.concat_view),
    path('save/',views.save_concat),
]