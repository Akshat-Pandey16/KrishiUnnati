from . import views
from django.urls import path

urlpatterns = [
    path("weather", views.input, name="weather"),
    path("weatherresult", views.result, name="weatherresult"),
]
