from django.urls import path
from .views import *


urlpatterns = [
    path('', PostsHome.as_view(), name='PostsHome'),
    path('add_page/', AddPage.as_view(), name='AddPage'),
    path('<slug:post_slug>/', Post.as_view(), name='post')
]
