from calorie_calculator.models import Menu
from posts.models import Posts


class DataMixin:
    paginate_by = 2

    def get_user_context(self, **kwargs):
        context = kwargs
        last_posts = Posts.objects.all().filter(is_published=True).order_by('-time_create')[:6]
        menu = Menu.objects.all()
        context['menu'] = menu
        context['last_posts'] = last_posts
        
            
        return context
    

    