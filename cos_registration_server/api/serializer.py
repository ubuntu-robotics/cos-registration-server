import json

from devices.models import Device
from rest_framework import serializers
from rest_framework.validators import UniqueValidator


class DeviceSerializer(serializers.Serializer):
    uid = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=Device.objects.all())],
    )
    creation_date = serializers.DateTimeField(read_only=True)
    address = serializers.IPAddressField(required=True)
    grafana_dashboards = serializers.JSONField(required=False)

    def create(self, validated_data):
        return Device.objects.create(**validated_data)

    def update(self, instance, validated_data):
        address = validated_data.get("address", instance.address)
        instance.address = address
        grafana_dashboards = validated_data.get(
            "grafana_dashboards", instance.grafana_dashboards
        )
        instance.grafana_dashboards = grafana_dashboards
        instance.save()
        return instance

    def validate_grafana_dashboards(self, value):
        if isinstance(value, str):
            try:
                dashboards = json.loads(value)
            except json.JSONDecodeError:
                raise serializers.ValidationError(
                    "Failed to load grafana_dashboards as json."
                )
        else:
            dashboards = value
        if not isinstance(dashboards, list):
            raise serializers.ValidationError(
                "gafana_dashboards is not a supported format (list)."
            )
        return dashboards
