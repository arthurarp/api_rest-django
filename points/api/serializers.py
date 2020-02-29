from rest_framework.serializers import ModelSerializer
from points.models import Points

class PointsSerializer(ModelSerializer):
    class Meta:
        model = Points
        fields = ('id', 'name', 'description', 'approve', 'attractions', 'comments', 'adress')