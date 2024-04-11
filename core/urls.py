from django.urls import path
from .views import(
    LandingPageView,
    HomeView, 
    ChatListView, 
    ChatDetailView,
    MessageListView,
)

urlpatterns = [
    path('', LandingPageView.as_view(), name='landing_page'),
    path('app/', HomeView.as_view(), name='home'),
    path('app/chats/', ChatListView.as_view(), name='chat_list'),
    path('app/chats/<int:chat_id>/', ChatDetailView.as_view(), name='chat_detail'),
    path('app/chats/<int:chat_id>/messages/', MessageListView.as_view(), name='message_list'),
]