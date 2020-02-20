from rest_framework.viewsets import ModelViewSet
from points.models import Points
from .serializers import PointsSerializer

class PointsViewSet(ModelViewSet):
    queryset = Points.objects.all()
    serializer_class = PointsSerializer