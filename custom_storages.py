# we want to store our media files on s3 as well as our static files thus we create this file

from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage

class StaticStorage(S3Boto3Storage):
  location = settings.STATICFILES_LOCATION

class MediaStorage(S3Boto3Storage):
  location = settings.MEDIAFILES_LOCATION

