from rest_framework import views, viewsets
from rest_framework.response import Response

from apps.contracts.models import tasks, Contract
from apps.contracts.serializer import TaskSerializer, ContractSerializer, CompareJsonSerializer


class TaskAPIView(views.APIView):
    permission_classes = []
    serializer_class = TaskSerializer

    def list(self, request):
        serializer = TaskSerializer(
            instance=tasks.values(), many=True)
        return Response(serializer.data)


class ContractViewSet(viewsets.ModelViewSet):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    http_method_names = ('get', 'post','delete')

class CompareJsonAPIView(views.APIView):
    http_method_names = ('get',)
    def get(self,request,format=None):
        serializer = CompareJsonSerializer(data=request.data)
