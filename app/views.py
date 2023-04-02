import logging

from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView

from app.serializers import AllureResultsSerializer, AllureReportSerializer

logger = logging.getLogger(__name__)


class ResultListView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    @swagger_auto_schema(request_body=AllureResultsSerializer,
                         # responses={201: UploadResults()},
                         operation_description="Upload allure results")
    def post(self, request):
        logger.debug(f"Upload allure results")

        serializer = AllureResultsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReportListView(APIView):

    @swagger_auto_schema(request_body=AllureReportSerializer,
                         # responses={201: UploadResults()},
                         operation_description="Generate report")
    def post(self, request):
        logger.debug(f"POST allure report: {request.data}")

        serializer = AllureReportSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
