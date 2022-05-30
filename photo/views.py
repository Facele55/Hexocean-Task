from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response

from photo.models import Photo
from .serializer import PhotoSerializer, CustomPhotoSerializer


class PhotoListView(ListCreateAPIView):
    """
    View class for displaying a list of user's `Photo` objects and
    creating new `Photo' object using POST method.
    The default permission setting for the whole project
    is IsAuthenticated.
    """
    def get_queryset(self):
        user = self.request.user
        return Photo.objects.filter(owner=user).order_by('-pk')

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CustomPhotoSerializer
        return PhotoSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def post(self, request, *args, **kwargs):
        serializer = PhotoSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
