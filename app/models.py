import logging
import shutil
import uuid

from django.db import models

logger = logging.getLogger(__name__)


class AllureResult(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    path = models.FileField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def delete(self, *args, **kwargs):
        logger.info(f"Delete results {self.id}")
        try:
            shutil.rmtree(f"static/results/{self.id}")
        except FileNotFoundError as ex:
            logger.error(f"File was not deleted for result: {self.id}:\n{ex}")
        super().delete(*args, **kwargs)


class AllureReport(models.Model):
    service_name = models.CharField(max_length=100)
    env = models.CharField(max_length=20)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    path = models.CharField(max_length=100)
    result = models.OneToOneField(AllureResult, on_delete=models.CASCADE, related_name="result_info")

    def delete(self, *args, **kwargs):
        logger.info(f"Delete report by path: {self.path}")
        try:
            shutil.rmtree(f"static/reports/{self.result.id}")
        except FileNotFoundError as ex:
            logger.error(f"File was not deleted for report: {self.result.id}:\n{ex}")
        super().delete(*args, **kwargs)
