from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about')
   # path('posts/', Posts.as_view(), name='posts'),
   # path('polls/', Polls.as_view(), name='polls'),
]