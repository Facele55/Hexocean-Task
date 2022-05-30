from easy_thumbnails.files import get_thumbnailer
from easy_thumbnails_rest.serializers import ThumbnailerJSONSerializer
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from hexocean.settings import THUMBNAIL_ALIASES
from photo.models import Photo


class PhotoSerializer(ModelSerializer):
    """
    Photo Serializer to show all photos and add new photo.
    """
    image = ThumbnailerJSONSerializer(alias="")

    class Meta:
        model = Photo
        fields = '__all__'
        read_only_fields = ('id', 'owner',)


class CustomPhotoSerializer(ModelSerializer):
    """
    Custom serializing photos.
    Based on user's tier fields will return photo with corresponding
    height or none.
    """
    original = serializers.SerializerMethodField()
    small_thumbnail = serializers.SerializerMethodField()
    medium_thumbnail = serializers.SerializerMethodField()
    hd_thumbnail = serializers.SerializerMethodField()
    full_hd_thumbnail = serializers.SerializerMethodField()
    custom_size_thumbnail = serializers.SerializerMethodField()

    def get_small_thumbnail(self, obj):
        request = self.context.get('request')
        options = THUMBNAIL_ALIASES[""]["small_thumbnail"]
        thumb_url = get_thumbnailer(obj.image).get_thumbnail(options).url
        if obj.owner.tier.pixel_height_200:
            return request.build_absolute_uri(thumb_url)
        else:
            return None

    def get_medium_thumbnail(self, obj):
        request = self.context.get('request')
        options = THUMBNAIL_ALIASES[""]["medium_thumbnail"]
        thumb_url = get_thumbnailer(obj.image).get_thumbnail(options).url
        if obj.owner.tier.pixel_height_400:
            return request.build_absolute_uri(thumb_url)
        else:
            return None

    def get_hd_thumbnail(self, obj):
        request = self.context.get('request')
        options = THUMBNAIL_ALIASES[""]["hd_thumbnail"]
        thumb_url = get_thumbnailer(obj.image).get_thumbnail(options).url
        if obj.owner.tier.pixel_height_hd:
            return request.build_absolute_uri(thumb_url)
        else:
            return None

    def get_full_hd_thumbnail(self, obj):
        request = self.context.get('request')
        options = THUMBNAIL_ALIASES[""]["full_hd_thumbnail"]
        thumb_url = get_thumbnailer(obj.image).get_thumbnail(options).url
        if obj.owner.tier.pixel_height_full_hd:
            return request.build_absolute_uri(thumb_url)
        else:
            return None

    def get_original(self, obj):
        request = self.context.get('request')
        thumb_url = get_thumbnailer(obj.image).url
        if obj.owner.tier.can_see_original:
            return request.build_absolute_uri(thumb_url)
        else:
            return None

    def get_custom_size_thumbnail(self, obj):
        request = self.context.get('request')
        size = obj.owner.tier.custom_size
        if obj.owner.tier.custom_size:
            thumbnail_options = ({'size': (size, 0), 'crop': True})
            thumb_url = get_thumbnailer(obj.image).get_thumbnail(thumbnail_options).url
            return request.build_absolute_uri(thumb_url)
        else:
            return None

    class Meta:
        model = Photo
        fields = ['id', 'owner', 'small_thumbnail', 'medium_thumbnail', 'hd_thumbnail', 'full_hd_thumbnail', 'original',
                  'custom_size_thumbnail']
        read_only_fields = fields
