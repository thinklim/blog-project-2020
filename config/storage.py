from storages.backends.s3boto3 import S3Boto3Storage


class S3StaticStorage(S3Boto3Storage):
    location = 'static_develop'

class S3MediaStorage(S3Boto3Storage):
    location = 'media'