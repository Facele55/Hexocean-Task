from django.contrib import admin
from easy_thumbnails.fields import ThumbnailerField
from easy_thumbnails.widgets import ImageClearableFileInput

from .models import CustomUser, Photo, Tier


admin.site.register(Tier)
admin.site.register(CustomUser)
admin.site.register(Photo)

