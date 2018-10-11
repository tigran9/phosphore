import json

from jsondiff import diff
from rest_framework import serializers
from rest_framework.fields import JSONField

from apps.contracts.models import Task, Contract


class TaskSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=256)
    owner = serializers.CharField(max_length=256)

    # status = serializers.ChoiceField(choices=, default='New')

    def create(self, validated_data):
        return Task(id=None, **validated_data)

    def update(self, instance, validated_data):
        for field, value in validated_data.items():
            setattr(instance, field, value)
        return instance


class ContractSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    name = serializers.CharField(max_length=255)
    data = serializers.JSONField(binary=False)

    def create(self, validated_data, *args, **kwargs):

        contract = Contract.objects.create(name=validated_data['name'], data=validated_data['data'])
        contract.save()
        return contract

    class Meta:
        model = Contract
        fields = [
            'id',
            'name',
            'data',
        ]

class CompareJsonSerializer(serializers.ModelSerializer):
    first_json = serializers.JSONField(binary=False)
    second_json = serializers.JSONField(binary=False)
    def validate(self, attrs):
        success = diff(attrs['first_json'],attrs['second_json'])
        if success
    class Meta:
        fields = [
            'first_json',
            'second_json',
        ]