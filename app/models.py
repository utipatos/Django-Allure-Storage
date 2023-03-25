import logging
import uuid

from django.db import models

logger = logging.getLogger(__name__)


class AllureResult(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    path = models.FileField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
