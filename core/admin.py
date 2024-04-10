# from django.contrib import admin
# from .models import Chat, Message

# @admin.register(Chat)
# class ChatAdmin(admin.ModelAdmin):
#     list_display = ('name', 'created_at', 'updated_at')
#     list_filter = ('created_at', 'updated_at')
#     search_fields = ('name',)

# @admin.register(Message)
# class MessageAdmin(admin.ModelAdmin):
#     list_display = ('chat', 'sender', 'created_at')
#     list_filter = ('created_at',)
#     search_fields = ('text',)

from django.contrib import admin
from .models import Chat, Message

admin.site.register(Chat)
admin.site.register(Message)