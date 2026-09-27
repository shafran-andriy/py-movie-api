from django.urls import path
from cinema.views import cinema_list, cinema_detail

app_name = "cinema"

urlpatterns = [
    path("/movies/", cinema_list, name="bus_list"),
    path("/movies/<int:pk>", cinema_detail, name="bus_detail"),
]
