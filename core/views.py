from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Chat  # Assuming you have a Chat model

class HomeView(LoginRequiredMixin, TemplateView):
    login_url = 'accounts/login/'  # Redirect to your login route
    redirect_field_name = 'redirect_to'

    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['chats'] = Chat.objects.all()  # Assuming you have a Chat model
        return context

# # Assuming you have a Message model with a foreign key to Chat that stores each message
# from .models import Message

# class ChatMessagesView(TemplateView):
#     def get(self, request, *args, **kwargs):
#         chat_id = request.GET.get('chat_id')
#         chat = get_object_or_404(Chat, id=chat_id)
#         messages = Message.objects.filter(chat=chat).values('text', 'created_at')
#         return JsonResponse(list(messages), safe=False)

# # Assuming you also want to handle sending messages
# from django.views import View
# from django.utils.decorators import method_decorator
# from django.views.decorators.csrf import csrf_exempt

# @method_decorator(csrf_exempt, name='dispatch')  # Be careful with CSRF. It's usually not a good idea to exempt it.
# class SendMessageView(View):
#     def post(self, request, *args, **kwargs):
#         chat_id = request.POST.get('chat_id')
#         message_text = request.POST.get('message')
#         chat = get_object_or_404(Chat, id=chat_id)
#         # Here you would save the message to the database
#         message = Message.objects.create(chat=chat, text=message_text)
#         return JsonResponse({'status': 'success', 'message': {'text': message.text, 'created_at': message.created_at}})


# # views.py
# from django.views import View
# from django.http import HttpResponseRedirect
# from django.urls import reverse
# from .models import Chat

# class CreateChatView(View):
#     def post(self, request, *args, **kwargs):
#         chat_name = request.POST.get('chat_name')
#         if chat_name:
#             chat, created = Chat.objects.get_or_create(name=chat_name)
#             if created:
#                 chat.participants.add(request.user)
#                 # Redirect to the chat room or home page where the new chat is visible
#                 return HttpResponseRedirect(reverse('home'))
#         # Redirect back to home if no chat_name is provided or the chat already exists
#         return HttpResponseRedirect(reverse('home'))

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Chat, Folder
from .serializers import ChatSerializer, FolderSerializer
from django.http import Http404

class ChatListCreateAPIView(APIView):
    def get(self, request):
        chats = Chat.objects.all()
        serializer = ChatSerializer(chats, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ChatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class ChatRetrieveUpdateDestroyAPIView(APIView):
    def get_object(self, pk):
        try:
            return Chat.objects.get(pk=pk)
        except Chat.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        chat = self.get_object(pk)
        serializer = ChatSerializer(chat)
        return Response(serializer.data)

    def put(self, request, pk):
        chat = self.get_object(pk)
        serializer = ChatSerializer(chat, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        chat = self.get_object(pk)
        chat.delete()
        return Response(status=204)
