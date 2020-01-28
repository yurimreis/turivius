from message_turivius.models import MessageTurivius
from rest_framework.serializers import ModelSerializer


class MessageSerializer(ModelSerializer):
    class Meta:
        model = MessageTurivius
        fields = ('id', 'title', 'text')