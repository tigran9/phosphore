from rest_framework import viewsets

from apps.users.models import User
from apps.users.serializer import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = ()
    http_method_names = ('get', 'post', 'put', 'patch',)
