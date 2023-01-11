from django.shortcuts import render
from rest_framework import generics
from .models import Message, TelegramToken
from .serializers import CreateMessageSerializer, GetAllMessagesSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .management.commands.bot import send_message
import uuid
from rest_framework import status

class MessageCreateAPI(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return Message.objects.filter(user = self.request.user)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return GetAllMessagesSerializer
        else:
            return CreateMessageSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        try:
            self.perform_create(serializer)
            response_data = serializer.data
            response_status=status.HTTP_201_CREATED
        except TelegramToken.DoesNotExist:
            response_data = {'error':'Произошла ошибка, вы не зарегистрировали токен'}
            response_data.update(serializer.data)
            response_status=status.HTTP_400_BAD_REQUEST
        finally:
            headers = self.get_success_headers(serializer.data)
            return Response(response_data, status=response_status, headers=headers)

    def perform_create(self, serializer):
        token = TelegramToken.objects.get(user = self.request.user)
        serializer.save(user=self.request.user)
        message = '{0}, я получил от тебя сообщение:\n{1}'.format(token.telegram_username, 
                                                                serializer.data['message'])
        send_message(token.telegram_chat_id, message)


class GetTokenAPI(APIView):
    permission_classes = (IsAuthenticated, )
    
    def get(self, request):
        token = TelegramToken.objects.get_or_create(user = self.request.user,
                                                    defaults={'telegram_token': str(uuid.uuid4())})[0]
        return Response({'telegram_token':token.telegram_token})
