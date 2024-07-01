from rest_framework import serializers
from .models import FileUpload

class FileUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileUpload
        fields = ('file', 'name')
    def create(self, validated_data):
        return FileUpload.objects.create(**validated_data)
