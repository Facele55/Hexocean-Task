from django.urls import path

from photo.views import PhotoListView


app_name = 'photo'

urlpatterns = [
    path('', PhotoListView.as_view(), name="photo_list"),
]
