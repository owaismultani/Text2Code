from django.urls import path
# from .views import HomeView, ChatMessagesView, SendMessageView, CreateChatView
from .views import HomeView
from .views import ChatListCreateAPIView, ChatRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    # path('get_messages/', ChatMessagesView.as_view(), name='get_messages'),
    # path('send_message/', SendMessageView.as_view(), name='send_message'),
    # path('create_chat/', CreateChatView.as_view(), name='create_chat'),
    path('chats/', ChatListCreateAPIView.as_view(), name='chat-list-create'),
    path('chats/<int:pk>/', ChatRetrieveUpdateDestroyAPIView.as_view(), name='chat-retrieve-update-destroy'),

]
