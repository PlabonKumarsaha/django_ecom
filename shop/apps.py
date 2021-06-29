from django.apps import AppConfig
from .models import Products
from .models import Oder


class ShopConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'shop'
