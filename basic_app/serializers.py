from rest_framework import serializers

from basic_app import models


class MarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Mark
        fields = '__all__'


class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Model1
        fields = '__all__'


class FuelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Fuel1
        fields = '__all__'


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Upload_File
        fields = '__all__'