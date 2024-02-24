from django.urls import path
from .views import RoomView

urlpatterns = [
    path("all_rooms", RoomView.as_view(), name="api_list_rooms")
]
