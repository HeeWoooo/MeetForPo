from django.urls import path, include
from .views import RoomsAPIMixins, RoomAPIMixins

urlpatterns = [
    path("mixin/rooms/", RoomsAPIMixins.as_view()),
    path("mixin/rooms/<str:id>", RoomAPIMixins.as_view()),
]