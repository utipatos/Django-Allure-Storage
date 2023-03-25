from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView

import logging

from app.serializers import AllureResultsSerializer

logger = logging.getLogger(__name__)


class ResultListView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    @swagger_auto_schema(request_body=AllureResultsSerializer,
                         # responses={201: UploadResults()},
                         operation_id="create_wallet_creation_request",
                         operation_description="Create wallet creation request")
    def post(self, request):
        logger.debug(f"Upload allure results")
        serializer = AllureResultsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
