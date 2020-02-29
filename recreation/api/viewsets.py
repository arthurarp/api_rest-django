from rest_framework.viewsets import ModelViewSet
from recreation.models import Recreation
from .serializers import RecreationsSerializers

class RecreationsViewSet(ModelViewSet):
    queryset = Recreation.objects.all()
    serializer_class = RecreationsSerializers