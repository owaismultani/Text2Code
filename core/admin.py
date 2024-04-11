"""
This file is used to register the models in the admin panel.
"""
from django.contrib import admin
from .models import Chat, Message

admin.site.register(Chat)
admin.site.register(Message)