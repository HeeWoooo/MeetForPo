
from django.shortcuts import render
from rest_framework import generics, mixins, viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from .models import Room
from .serializers import RoomSerializer
import uuid


def create_code(string_length = 10):
    random = str(uuid.uuid4())
    random = random.upper()
    random = random.replace("=", "")

class RoomsAPIMixins(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class RoomAPIMixins(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    lookup_field = 'room_code'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class RoomsAPI(APIView):
    def get(self, request):
        rooms = Room.objects.all()
        serializer = RoomSerializer(rooms, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        request.data["room_code"] = create_code(8)
        serializer = RoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
