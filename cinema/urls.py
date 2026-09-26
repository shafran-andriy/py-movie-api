from django.urls import path
from cinema.views import cinema_list, cinema_detail

app_name = "cinema"

urlpatterns = [
    path("cinemas/", cinema_list, name="bus_list"),
    path("cinemas/<int:pk>", cinema_detail, name="bus_detail"),
]
