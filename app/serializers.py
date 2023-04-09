import logging
import os
import shutil

from rest_framework import serializers

from app.models import AllureResult, AllureReport

logger = logging.getLogger(__name__)


class AllureResultsSerializer(serializers.ModelSerializer):
    path = serializers.FileField()
    id = serializers.UUIDField(read_only=True)

    class Meta:
        model = AllureResult
        fields = ('id', 'path',)

    def create(self, validated_data):
        path = validated_data.get('path', None)
        logger.info(f"Storing report with path: {path} and id: {validated_data.get('id')}")
        instance = super(AllureResultsSerializer, self).create(validated_data)

        if path:
            new_path = f"static/results/{instance.id}/{path.name}"
            instance.path.save(new_path, path)
            logger.info(f"Unpack file {new_path}")
            shutil.unpack_archive(new_path, extract_dir=f"static/results/{instance.id}")

            os.remove(path.name)
            os.remove(f"{new_path}")

        return instance


class AllureReportSerializer(serializers.ModelSerializer):
    path = serializers.CharField(read_only=True)
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = AllureReport
        fields = ('id', 'result', 'env', 'service_name', 'path')

    def create(self, validated_data):
        logger.info(f"Generating report: {validated_data}")

        result_id = validated_data.get('result').id
        validated_data["path"] = f"/static/reports/{result_id}/index.html"

        instance = super(AllureReportSerializer, self).create(validated_data)

        if result_id:
            os.system(
                f'allure generate --report-path static/results/{result_id} --report-dir static/reports/{result_id}')

        return instance
