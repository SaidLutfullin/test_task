from django.conf import settings
from django.db import models
from django.utils import timezone

class Message(models.Model):
    date = models.DateField(default=timezone.now, verbose_name='Дата')
    message = models.TextField(blank=True, verbose_name='Сообщение')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return self.message

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'


class TelegramToken(models.Model):
    telegram_token = models.TextField(verbose_name='Телеграм токен')
    telegram_chat_id = models.IntegerField(null=True, verbose_name='ID чата')
    telegram_username = models.TextField(null=True, verbose_name='Имя пользователя телеграм')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Телеграм токен'
        verbose_name_plural = 'Телеграм токены'