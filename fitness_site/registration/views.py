from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from utils import DataMixin
from .forms import *
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login
from fitness_site import settings


class RegisterUser(DataMixin, CreateView):
    form_class = RegistrationUserForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        return dict(list(context.items())+ list(c_def.items()))

    def form_valid(self, form):
        user = form.save(commit=False)
        
        if not form.cleaned_data['avatar']:
            user.avatar = settings.DEFAULT_AVATAR  # Здесь DEFAULT_AVATAR - это путь к вашему изображению по умолчанию
        
        user.save()
        login(self.request, user)
        
        return redirect('PostsHome')
    

class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'registration/login.html'
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Авторизация')
        return dict(list(context.items()) + list(c_def.items()))
    
    def get_success_url(self):
        return reverse_lazy('PostsHome')



def logout_user(request):
    logout(request) 
    return redirect('PostsHome') 