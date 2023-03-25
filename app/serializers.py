import logging
import os
import uuid

from django.core.files.uploadedfile import UploadedFile
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework import serializers

from app.models import AllureResult

logger = logging.getLogger(__name__)


class AllureResultsSerializer(serializers.ModelSerializer):
    path = serializers.FileField()
    id = serializers.UUIDField(read_only=True)

    class Meta:
        model = AllureResult
        fields = ('path', 'id', )

    def create(self, validated_data):
        path = validated_data.get('path', None)
        logger.info(f"Storing report with path: {path} and id: {validated_data.get('id')}")
        instance = super(AllureResultsSerializer, self).create(validated_data)

        if path:
            instance.path.save(f"static/results/{instance.id}/{path.name}", path)
            os.remove(path.name)

        return instance
