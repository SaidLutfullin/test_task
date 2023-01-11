from django.core.management.base import BaseCommand
from applications.telegram_interaction.models import TelegramToken
from django.conf import settings
import telebot

bot = telebot.TeleBot(settings.TELEGRAM_BOT_TOKEN, parse_mode=None)

class Command(BaseCommand):
    help = 'Telegram Bot'

    def handle(self, *args, **kwargs):
        bot.enable_save_next_step_handlers(delay=2)
        bot.load_next_step_handlers()
        bot.infinity_polling()


@bot.message_handler(func=lambda m: True)
def send_token(message):
    successfull = save_chat_id(message.text, message.chat.id, message.chat.username)
    if successfull:
        response_message = 'Вы успешно авторизованы'
    else:
        response_message = 'Неверный токен'
    send_message(message.chat.id, response_message)


def save_chat_id(token, chat_id, usermane):
    try:
        token = TelegramToken.objects.get(telegram_token=token)
        token.telegram_chat_id = chat_id
        token.telegram_username = usermane
        token.save()
        return True
    except TelegramToken.DoesNotExist:
        return False


def send_message(chat_id, message):
	bot.send_message(chat_id, message)
