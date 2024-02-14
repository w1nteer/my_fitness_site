from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from utils import DataMixin
from .models import *
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import *
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.urls import reverse


class PostsHome(DataMixin, ListView):
    model = Posts
    template_name = 'posts/posts_home.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Posts.objects.all().filter(is_published=True).select_related('cat')
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        user_context = self.get_user_context(title='Посты')
        return dict(list(context.items()) + list(user_context.items()))



class Post(DetailView, DataMixin):
    model = Posts
    template_name = 'posts/show_post.html'
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        user_context = self.get_user_context(title=self.get_object().title)

        comments = Comment.objects.filter(post=self.object)
        paginator = Paginator(comments, 5)  # Здесь 5 - количество комментариев на одной странице
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['comments'] = page_obj

        form = CommentForm()
        context['form'] = form

        return dict(list(context.items()) + list(user_context.items()))
    
    def post(self, request, *args, **kwargs):
        post = self.get_object()
        user = request.user
        content = request.POST.get('content')

        
        Comment.objects.create(post=post, user=user, content=content)

        return HttpResponseRedirect(reverse('post', kwargs={'post_slug': post.slug}))


class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPageForm
    template_name = 'posts/add_page.html'
    success_url = reverse_lazy('PostsHome')
    login_url = reverse_lazy('register')

    def form_valid(self, form):
        form.instance.author = self.request.user

        # Создание slug на основе title с преобразованием русских символов
        title = form.cleaned_data.get('title')
        slug = slugify(unidecode(title))
        form.instance.slug = slug

        return super().form_valid(form)


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Создание статьи')

        return dict(list(context.items()) + list(c_def.items()))  
    