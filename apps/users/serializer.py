from rest_framework import serializers

from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=255, allow_null=True, allow_blank=False)
    last_name = serializers.CharField(max_length=255, allow_null=True, allow_blank=False)
    username = serializers.CharField(max_length=255, allow_null=True, allow_blank=False)
    email = serializers.EmailField(required=True, max_length=255, allow_null=False,
                                   allow_blank=False)
    id = serializers.ReadOnlyField()

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'email']
