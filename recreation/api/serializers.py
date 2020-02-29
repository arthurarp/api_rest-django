from rest_framework.serializers import ModelSerializer
from recreation.models import Recreation

class RecreationsSerializers(ModelSerializer):
    class Meta:
        model = Recreation
        fields = ('id', 'name', 'description', 'opening_hours', 'minimum_age')