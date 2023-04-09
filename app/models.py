import logging
import uuid

from django.db import models

logger = logging.getLogger(__name__)


class AllureResult(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    path = models.FileField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


class AllureReport(models.Model):
    service_name = models.CharField(max_length=100)
    env = models.CharField(max_length=20)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    path = models.CharField(max_length=100)

    result = models.OneToOneField(AllureResult, on_delete=models.CASCADE, related_name="result_info")