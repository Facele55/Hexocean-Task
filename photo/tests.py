from io import BytesIO

from PIL import Image
from django.core.files.base import File
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from photo.models import CustomUser, Photo


class CustomUserModelTest(TestCase):
	"""
	Testing model CustomUser for Assertion equality
	"""
	@classmethod
	def setUpTestData(cls):
		# Set up non-modified objects used by all test methods
		CustomUser.objects.create(username='test_user')

	def test_username_label(self):
		user = CustomUser.objects.get(id=1)
		field_label = user._meta.get_field('username').verbose_name
		self.assertEqual(field_label, 'username')

	def test_object_name(self):
		user = CustomUser.objects.get(id=1)
		expected_object_name = f"{user.username}"
		self.assertEqual(str(user), expected_object_name)


class ModelPhotoTest(TestCase):
	"""
	Testing model Photo for Assertion equality
	"""
	@classmethod
	def setUpTestData(cls):
		# Set up non-modified objects used by all test methods
		CustomUser.objects.create(username='test_user')
		Photo.objects.create(owner_id=1, image='avatar.png')

	def test_username_label(self):
		photo = Photo.objects.get(id=1)
		field_label = photo.owner
		self.assertEqual(str(field_label), 'test_user')

	def test_object_name(self):
		photo = Photo.objects.get(id=1)
		self.assertEqual(str(photo.image), 'avatar.png')


class TestListCreatePhoto(APITestCase):
	"""
	To submit photo user have to be authorized.
	If not user will get 403 (FORBIDDEN) status code
	"""

	def test_submit_photo_no_auth(self):
		"""
		User have to be authorized to add photo
		"""
		image = create_image_file('image.png')
		sample_photo = {"user": "username", "image": image}
		response = self.client.post(reverse("photo:photo_list"), sample_photo)
		self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


def create_image_file(name: str, ext='png', size=(500, 500), color=(256, 0, 0)) -> File:
	"""
	Creating dummy image file
	:param name:
	:param ext:
	:param size:
	:param color:
	:return:
	"""
	file_obj = BytesIO()
	image = Image.new("RGBA", size=size, color=color)
	image.save(file_obj, ext)
	file_obj.seek(0)
	return File(file_obj, name=name)
