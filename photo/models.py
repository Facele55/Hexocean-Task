from django.contrib.auth.models import AbstractUser
from django.db import models
from easy_thumbnails.fields import ThumbnailerField


def user_directory_path(instance, filename):
	"""
	Organize photos in media folder by creating user ID folder.
	Name, username, email can be changed but not user ID.
	:param instance:
	:param filename:
	:return:
	"""
	return 'user_{0}/{1}'.format(instance.owner.id, filename)


class Tier(models.Model):
	"""
	Tier instance
	"""
	name = models.CharField(max_length=255)
	pixel_height_200 = models.BooleanField(default=False)
	pixel_height_400 = models.BooleanField(default=False)
	pixel_height_hd = models.BooleanField(default=False)
	pixel_height_full_hd = models.BooleanField(default=False)
	can_see_original = models.BooleanField(default=False)
	custom_size = models.IntegerField(null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f"{self.name}"


class CustomUser(AbstractUser):
	"""
	CustomUser Instance
	"""
	tier = models.ForeignKey(Tier, on_delete=models.CASCADE, related_name='tier', null=True)

	def __str__(self):
		return self.get_username()


class Photo(models.Model):
	"""
	Photo Instance
	"""
	image = ThumbnailerField(upload_to=user_directory_path)
	owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='owner', null=True)
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.image.url
