from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Chat(models.Model):
    """
    Chat model is used to store the chat details.
    """
    title = models.CharField(max_length=255)
    code = models.CharField(max_length=1000000, default='')
    language = models.CharField(max_length=255, default='python')
    suggested_language = models.CharField(max_length=255, default='')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chats')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        """
        Meta class for the Chat model.
        """
        ordering = ['-created_at']
        db_table = 'chats'
    
    def save(self, *args, **kwargs):
        """
        Override the save method to set the title if it is not set.
        """
        # Flag to determine if the instance is new
        creating = not self.pk
        super().save(*args, **kwargs)  # Perform the initial save to generate an id

        if creating and not self.title:
            self.title = f'New Chat {self.pk}'
            super().save(update_fields=['title'])  # Save again with the updated title

    def __str__(self):
        return self.title

class Message(models.Model):
    """
    Message model is used to store the chat messages.
    """
    chat = models.ForeignKey(Chat, related_name='messages', on_delete=models.CASCADE)
    text = models.TextField()
    role = models.CharField(max_length=255, default='user')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages')

    class Meta:
        """
        Meta class for the Message model.
        """
        ordering = ['created_at']
        db_table = 'messages'

    def __str__(self):
        return self.text
