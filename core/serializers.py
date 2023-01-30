from rest_framework import serializers

from .models import FrameworkModel


class FrameworkSerializer(serializers.ModelSerializer):

    class Meta:
        model = FrameworkModel
        fields = '__all__'
