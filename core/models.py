# from django.db import models
# from django.contrib.auth import get_user_model

# User = get_user_model()

# class Chat(models.Model):
#     name = models.CharField(max_length=255)
#     participants = models.ManyToManyField(User, related_name='chats')
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.name

# # class Message(models.Model):
# #     chat = models.ForeignKey(Chat, related_name='messages', on_delete=models.CASCADE)
# #     sender = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
# #     text = models.TextField()
# #     created_at = models.DateTimeField(auto_now_add=True)

# #     def __str__(self):
# #         return f'Message by {self.sender.username} in {self.chat.name}'

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Folder(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='children')

class Chat(models.Model):
    title = models.CharField(max_length=255)
    message = models.TextField()
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chats')
    updated_at = models.DateTimeField(auto_now=True)
