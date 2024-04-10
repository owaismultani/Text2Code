from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from .models import Chat, Message
from django.views.generic import ListView
from django.http import JsonResponse
from django.views import View
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .services import CodeGenerator

class HomeView(LoginRequiredMixin, TemplateView):
    login_url = 'accounts/login/'
    redirect_field_name = 'redirect_to'

    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['chats'] = Chat.objects.all()
        return context
    

class ChatListView(View):
    login_url = 'accounts/login/'
    redirect_field_name = 'redirect_to'
    model = Chat

    def get(self, request, *args, **kwargs):
        return HttpResponseRedirect(reverse('home'))
    
    def post(self, request, *args, **kwargs):
        chat = self.model.objects.create(created_by=request.user)
        return HttpResponseRedirect(reverse('chat_detail', args=(chat.id,)))


class ChatDetailView(View):
    login_url = 'accounts/login/'
    redirect_field_name = 'redirect_to'

    def get(self, request, *args, **kwargs):
        chats = Chat.objects.all()
        chat_id = kwargs['chat_id']
        chat = Chat.objects.get(id=chat_id)
        messages = Message.objects.filter(chat=chat)
        return render(request, 'core/chat.html', {'chat': chat, 'messages': messages, 'chats': chats, 'code': chat.code, 'language': chat.language})
    
    def post(self, request, *args, **kwargs):
        chat_id = kwargs['chat_id']
        method = request.POST.get('_method')
        if method == 'delete':
            return self.delete(request, *args, **kwargs)
        elif method == 'patch':
            return self.patch(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('chat_detail', args=(chat_id,)))
        
    
    def patch(self, request, *args, **kwargs):
        chat_id = kwargs['chat_id']
        chat = Chat.objects.get(id=chat_id)
        chat.title = request.POST.get('title', chat.title)
        chat.save()
        return HttpResponseRedirect(reverse('chat_detail', args=(chat.id,)))

    def delete(self, request, *args, **kwargs):
        chat_id = kwargs['chat_id']
        chat = Chat.objects.get(id=chat_id)
        chat.delete()
        return HttpResponseRedirect(reverse('chat_list'))

class MessageListView(View):
    login_url = 'accounts/login/'
    redirect_field_name = 'redirect_to'
    
    def post(self, request, *args, **kwargs):
        chat_id = kwargs['chat_id']
        chat = Chat.objects.get(id=chat_id)
        sender = request.user
        text = request.POST.get('text')
        Message.objects.create(chat=chat, sender=sender, text=text)
        messages = Message.objects.filter(chat=chat)
        message, code = self.get_suggestions(messages)
        if message:
            Message.objects.create(chat=chat, sender=sender, text=message)
        if code:
            Chat.objects.update(code=code)

        return HttpResponseRedirect(reverse('chat_detail', args=(chat.id,) ))


    def get_suggestions(self, messages):
        """
        Get suggestions from openai
        """
        code_generator = CodeGenerator(api_key='sk-')
        suggestion = code_generator.generate_code(messages)

        # split code and message by ``` separator and remove the last ``` separator
        message1, code, message2 = suggestion.split('```')
        code = code[:-3]
        message = message1 + message2
        return message, code


class GetLanguagesView(View):
    def get(self, request, *args, **kwargs):
        languages = [
            {'value': 'python', 'name': 'Python'},
            {'value': 'javascript', 'name': 'JavaScript'},
            {'value': 'java', 'name': 'Java'},
            {'value': 'c', 'name': 'C'},
            {'value': 'c++', 'name': 'C++'},
            {'value': 'c#', 'name': 'C#'},
            {'value': 'ruby', 'name': 'Ruby'},
            {'value': 'php', 'name': 'PHP'},
            {'value': 'go', 'name': 'Go'},
        ]
        return JsonResponse({'languages': languages})
