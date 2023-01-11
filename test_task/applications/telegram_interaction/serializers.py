from rest_framework import serializers
from .models import Message

class CreateMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('message', )


class GetAllMessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('message', 'date')