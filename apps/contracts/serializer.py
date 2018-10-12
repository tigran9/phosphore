import json
from jsondiff import diff
from rest_framework import serializers
from apps.contracts.models import Contract
import jsonschema
from jsonschema import validate as check_json


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
        success = diff(attrs['first_json'], attrs['second_json'])
        return success

    class Meta:
        fields = [
            'first_json',
            'second_json',
        ]


class JsonValidationSerializer(serializers.Serializer):
    j_values = serializers.JSONField(binary=False)
    scheme_id = serializers.CharField(max_length=255)

    def validate(self, attrs):
        if Contract.objects.filter(id=attrs['scheme_id']).first() is not None:
            json_schema = Contract.objects.filter(id=attrs['scheme_id']).first()
            print(json_schema.data)
            # return attrs
            for idx, item in enumerate(attrs["j_values"]["data"]):
                if (check_json(item, json_schema.data)):
                    return attrs["values"]["data"]
                else:
                    ve = jsonschema.exceptions.ValidationError
                    return serializers.ValidationError({"detail: {} item is not valid. error: {}".format(item, str(ve))}, )
            # print(dict(attrs))
            # jarray = json.loads({attrs["j_values"]["data"]})
            # for idx, item in enumerate(jarray):
            #     share = enumerate(attrs["j_values"]["data"])
            #     print(share)
            #     # while check_json(item, json_schema.data):
            #     #     return attrs
            #     # return serializers.ValidationError("detail: {} item is not valid.".format(item), )
            #     # if (check_json(item, json_schema.data)):
            #     #     return attrs["values"]["data"]
            #     # else:
            #     #     return serializers.ValidationError("detail: {} item is not valid.".format(item), )
            #     try:
            #         check_json(item, json_schema.data)
            #         return attrs
            #     except jsonschema.exceptions.ValidationError as ve:
            #         return serializers.ValidationError({"detail: {} item is not valid. error: {}".format(item, str(ve))}, )
            #
            #
        else:
            raise serializers.ValidationError("detail: json have not valid scheme.")

    class Meta:
        fields = [
            'j_values',
            'scheme_id',
        ]
