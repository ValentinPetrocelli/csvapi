from rest_framework import serializers

class CsvSerializer(serializers.Serializer):
    csvfile = serializers.FileField()