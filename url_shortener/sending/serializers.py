from rest_framework import serializers
from .models import Url

class UrlSerializer(serializers.ModelSerializer):
    random_string = serializers.ReadOnlyField()
    class Meta:
        model = Url
        fields = ['url','random_string']
        