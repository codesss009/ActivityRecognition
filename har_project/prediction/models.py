from django.db import models

class FileUpload(models.Model):
    file = models.FileField(upload_to='uploads/')
    name = models.CharField(max_length=100)
