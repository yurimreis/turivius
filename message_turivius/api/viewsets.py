from rest_framework.viewsets import ModelViewSet
from message_turivius.models import MessageTurivius
from .serializers import MessageSerializer

# Definição das operações
class MessageViewSet(ModelViewSet):
    queryset = MessageTurivius.objects.all()
    serializer_class = MessageSerializer