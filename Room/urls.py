from django.urls import path, include
from .views import RoomsAPIMixins, RoomsAPI, RoomAPIMixins

urlpatterns = [
    path("mixin/rooms/", RoomsAPIMixins.as_view()),
    path("cbv/rooms/", RoomsAPI.as_view()),
    path("mixin/room/<str:room_code>", RoomAPIMixins.as_view()),
]