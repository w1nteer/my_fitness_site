from django.contrib import admin
from .models import *


class PollAdmin(admin.ModelAdmin):
    list_display = ('id', 'question_text')
    list_display_links = ('question_text', )
    search_fields = ('question_text', 'id')
    

admin.site.register(Poll, PollAdmin)



class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'poll', 'choice_text', 'votes')
    list_display_links = ('choice_text', 'id')
    search_fields = ('choice_text', 'id', 'poll')
    

admin.site.register(Choice, ChoiceAdmin)
