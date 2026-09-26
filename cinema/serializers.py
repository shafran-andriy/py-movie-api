from rest_framework import serializers
from cinema.models import Cinema


class CinemaSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, max_length=255)
    duration = serializers.DateTimeField()

    def create(self, validated_data):
        return Cinema.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.duration = validated_data.get("duration", instance.duration)
        instance.save()
        return instance
