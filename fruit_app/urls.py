from django.urls import path
from . import views

urlpatterns = [
    path("", views.fruitlist, name="fruitlist"),
    path("info/", views.info, name="info"),
]
