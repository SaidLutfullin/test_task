from django.apps import AppConfig


class TelegramInteractionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'applications.telegram_interaction'
    verbose_name = 'Взаимодействие с телеграм ботом'
