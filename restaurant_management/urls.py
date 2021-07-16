from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from django.conf.urls.static import static
from django.conf import settings
from . import views

from django.conf.urls import url, include
from django.urls import register_converter


class SignedIntConverter:
    """
    Looks for naturals with 0 AND negative naturals. Any integer should do.
    """
    regex = '-?\d+'

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return str(value)


