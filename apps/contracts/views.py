from rest_framework import views, viewsets, status
from rest_framework.response import Response

from apps.contracts.models import  Contract
from apps.contracts.serializer import  ContractSerializer, CompareJsonSerializer, \
    JsonValidationSerializer


class ContractViewSet(viewsets.ModelViewSet):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    http_method_names = ('get', 'post', 'delete')


class CompareJsonAPIView(views.APIView):
    http_method_names = ('get',)

    def get(self, request, format=None):
        serializer = CompareJsonSerializer(data=request.data)


class JsonSchemeValidationAPIView(views.APIView):
    serializer_class = JsonValidationSerializer

    def get_serializer(self):
        return self.serializer_class()

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
