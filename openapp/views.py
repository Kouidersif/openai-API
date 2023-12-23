from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
# Create your views here.
from dotenv import load_dotenv
import os
from openai import OpenAI
import openai
from .models import ChatGptBot
load_dotenv()
from django.contrib.auth import authenticate, login
from django.views.generic import CreateView, DeleteView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import SignUpForm, UserLoginForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages




client = OpenAI(
    # This is the default and can be omitted
    api_key=os.getenv("OPENAI_API_KEY"),
)




def index(request):
    #check if user is authenticated
    if request.user.is_authenticated:
        if request.method == 'POST':
            #get user input from the form
            user_input = request.POST.get('userInput')
            #clean input from any white spaces
            clean_user_input = str(user_input).strip()
            #send request with user's prompt
            try:
                response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                            {
                                "role": "user",
                                "content": clean_user_input,
                            }
                        ],
                    )
                #get response
                
                bot_response = response.choices[0].message.content
                
                obj, created = ChatGptBot.objects.get_or_create(
                    user=request.user,
                    messageInput=clean_user_input,
                    bot_response=bot_response,
                )
            except openai.APIConnectionError as e:
                #Handle connection error here
                messages.warning(request, f"Failed to connect to OpenAI API, check your internet connection")
            except openai.RateLimitError as e:
                #Handle rate limit error (we recommend using exponential backoff)
                messages.warning(request, f"You exceeded your current quota, please check your plan and billing details.")
                messages.warning(request, f"If you are a developper change the API Key")
                

            return redirect(request.META['HTTP_REFERER'])
        else:
            #retrieve all messages belong to logged in user
            get_history = ChatGptBot.objects.filter(user=request.user)
            context = {'get_history':get_history}
            return render(request, 'index.html', context)
    else:
        return redirect("login")




class SignUp(CreateView):
    form_class = SignUpForm
    template_name = "users/register.html"
    def form_valid(self, form):
        response = super().form_valid(form)
        # Get the user's username and password in order to automatically authenticate user after registration
        username = form.cleaned_data['username']
        password = form.cleaned_data['password1']
        # Authenticate the user and log him/her in
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return response
    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.warning(self.request, f"{field}: {error}")
        return redirect(self.request.META['HTTP_REFERER'])
    def get_success_url(self):
        return reverse("main")



class LoginView(FormView):
    form_class = UserLoginForm
    template_name = "login.html"
    def form_valid(self, form):
        response = super().form_valid(form)
        # Get the user's username and password and authenticate
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        # Authenticate the user and log him/her in
        user = authenticate(username=username, password=password)
        login(self.request, user)
        messages.success(self.request, "You are logged in")
        return response
    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.warning(self.request, f"{error}")
        return redirect(self.request.META['HTTP_REFERER'])
    def get_success_url(self):
        return reverse("main")



@login_required
def DeleteHistory(request):
    chatGptobjs = ChatGptBot.objects.filter(user = request.user)
    chatGptobjs.delete()
    messages.success(request, "All messages have been deleted")
    return redirect(request.META['HTTP_REFERER'])


def logout_view(request):
    logout(request)
    messages.success(request, "Succesfully logged out")
    return redirect("main")