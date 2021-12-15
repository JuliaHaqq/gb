from typing import DefaultDict
from django.apps import AppConfig


class MainappConfig(AppConfig):
    Default_auto_field = 'django.db.models.BigAutoField'
    name = 'mainapp'
    