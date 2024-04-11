from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from .models import Chat, Message
from django.views import View
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .services import CodeGenerator
from django.conf import settings

OPENAI_API_KEY = settings.OPENAI_API_KEY


class LandingPageView(TemplateView):
    """
    LandingPageView is for the landing page of the application.
    This view inherits from the TemplateView class and uses the template 'core/landing_page.html'.
    This view does not require the user to be logged in.
    """
    template_name = 'core/landing_page.html'

class HomeView(LoginRequiredMixin, TemplateView):
    """
    HomeView is for the home page of the core application.
    This view inherits from the TemplateView class and uses the template 'core/home.html'.
    This view requires the user to be logged in.
    """
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        """
        Get the context data for the home page.
        """
        context = super().get_context_data(**kwargs)
        context['chats'] = Chat.objects.all()
        return context
    

class ChatListView(LoginRequiredMixin, View):
    """
    ChatListView is for the list of chats in the application.
    This view inherits from the View class.
    This view requires the user to be logged in.
    """
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
    model = Chat

    def get(self, request, *args, **kwargs):
        """
        Get the list of chats.
        """
        chats = self.model.objects.all()
        return render(request, 'core/home.html', {'chats': chats})
    
    def post(self, request, *args, **kwargs):
        """
        Create a new chat.
        """
        chat = self.model.objects.create(created_by=request.user)
        return HttpResponseRedirect(reverse('chat_detail', args=(chat.id,)))


class ChatDetailView(LoginRequiredMixin, View):
    """
    ChatDetailView is for the detail view of a chat.
    This view inherits from the View class.
    This view requires the user to be logged in.
    """
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'

    def get(self, request, *args, **kwargs):
        """
        Get the detail view of a chat.
        """
        chat_id = kwargs['chat_id']
        try:
            chat = Chat.objects.get(id=chat_id)
        except Chat.DoesNotExist:
            return render(request, 'core/page_not_found.html', {'chats': chats})
        
        messages = Message.objects.filter(chat=chat)
        chats = Chat.objects.all() # Get all chats for the sidebar

        return render(request, 'core/chat.html', {'chat': chat, 'messages': messages, 'chats': chats, 'code': chat.code, 'language': chat.language})
    
    def post(self, request, *args, **kwargs):
        """
        PATCH or DELETE is not supported by html forms.
        We receive the method from the form and handle it here.
        If the method is DELETE, we delete the chat.
        If the method is PATCH, we update the chat.
        All other methods are redirected to the chat detail view.
        """
        chat_id = kwargs['chat_id']
        method = request.POST.get('_method')
        if method == 'delete':
            return self.delete(request, *args, **kwargs)
        elif method == 'patch':
            return self.patch(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('chat_detail', args=(chat_id,)))
    
    def patch(self, request, *args, **kwargs):
        """
        Update the chat.
        """
        chat_id = kwargs['chat_id']
        chat = Chat.objects.get(id=chat_id)
        chat.title = request.POST.get('title', chat.title)
        chat.save()
        return HttpResponseRedirect(reverse('chat_detail', args=(chat.id,)))

    def delete(self, request, *args, **kwargs):
        """
        Delete the chat.
        """
        chat_id = kwargs['chat_id']
        chat = Chat.objects.get(id=chat_id)
        chat.delete()
        return HttpResponseRedirect(reverse('chat_list'))

class MessageListView(LoginRequiredMixin, View):
    """
    MessageListView is for the list of messages in a chat.
    This view inherits from the View class.
    This view requires the user to be logged in.
    """
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
    
    def post(self, request, *args, **kwargs):
        """
        Create a new message in a chat.
        It also generates a response from OpenAI and saves it as a message in the chat, along with the code and language.
        """
        chat_id = kwargs['chat_id']
        chat = Chat.objects.get(id=chat_id)
        sender = request.user
        text = request.POST.get('text')
        Message.objects.create(chat=chat, sender=sender, text=text)

        code_generator = CodeGenerator(api_key=OPENAI_API_KEY)
        generated_response = code_generator.generate_code(chat)
        
        if generated_response.get('message'):
            Message.objects.create(chat=chat, sender=sender, text=generated_response['message'], role='assistant')
        if generated_response.get('code'):
            Chat.objects.update(code=generated_response['code'])
        if generated_response.get('language'):
            Chat.objects.update(suggested_language=generated_response['language'])

        return HttpResponseRedirect(reverse('chat_detail', args=(chat.id,) ))


# Deprecated
# class GetLanguagesView(LoginRequiredMixin, View):
#     """
#     GetLanguagesView is for the list of languages that can be used in the application.
#     This view inherits from the View class.
#     This view requires the user to be logged in.
#     """
#     def get(self, request, *args, **kwargs):
#         languages = [
#             {'value': 'python', 'name': 'Python'},
#             {'value': 'javascript', 'name': 'JavaScript'},
#             {'value': 'java', 'name': 'Java'},
#             {'value': 'c', 'name': 'C'},
#             {'value': 'c++', 'name': 'C++'},
#             {'value': 'c#', 'name': 'C#'},
#             {'value': 'ruby', 'name': 'Ruby'},
#             {'value': 'php', 'name': 'PHP'},
#             {'value': 'go', 'name': 'Go'},
#         ]
#         return JsonResponse({'languages': languages})
