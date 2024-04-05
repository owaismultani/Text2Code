from rest_framework import serializers
from .models import Chat, Folder

class FolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Folder
        fields = '__all__'

class ChatSerializer(serializers.ModelSerializer):
    folder = FolderSerializer()

    class Meta:
        model = Chat
        fields = '__all__'
