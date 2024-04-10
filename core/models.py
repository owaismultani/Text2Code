from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Chat(models.Model):
    title = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chats')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['-created_at']
        db_table = 'chats'

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        # Flag to determine if the instance is new
        creating = not self.pk
        super().save(*args, **kwargs)  # Perform the initial save to generate an id

        if creating and not self.title:
            self.title = f'New Chat {self.pk}'
            super().save(update_fields=['title'])  # Save again with the updated title

class Message(models.Model):
    chat = models.ForeignKey(Chat, related_name='messages', on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages')

    class Meta:
        ordering = ['created_at']
        db_table = 'messages'

    def __str__(self):
        return self.text
