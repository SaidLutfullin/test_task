from django.contrib import admin
from .models import Message,TelegramToken


class MessageAdmin(admin.ModelAdmin):
    list_display = ('message', 'date', 'user') 
    list_display_links = ('message',)
admin.site.register(Message, MessageAdmin)


class TelegramTokenAdmin(admin.ModelAdmin):
    list_display = ('telegram_token', 'telegram_chat_id', 'telegram_username', 'user') 
    list_display_links = ('telegram_token', 'telegram_chat_id', 'telegram_username', 'user') 
admin.site.register(TelegramToken, TelegramTokenAdmin)