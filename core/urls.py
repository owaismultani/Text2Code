from django.urls import path
from .views import(
    HomeView, 
    ChatListView, 
    GetLanguagesView, 
    ChatDetailView,
    MessageListView
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('chats/', ChatListView.as_view(), name='chat_list'),
    path('chats/<int:chat_id>/', ChatDetailView.as_view(), name='chat_detail'),
    path('chats/<int:chat_id>/messages/', MessageListView.as_view(), name='message_list'),
    path('languages/', GetLanguagesView.as_view(), name='languages'),
]