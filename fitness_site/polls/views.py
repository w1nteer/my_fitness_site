from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from .models import *
from utils import DataMixin
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import TemplateView

class PollsView(LoginRequiredMixin, DataMixin, TemplateView):
    template_name = 'polls/polls.html'
    login_url = 'register'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_context = self.get_user_context()
        context.update(user_context)
        return context

    def post(self, request):
        if not request.user.is_authenticated:
            return redirect('register')

        question_id = request.POST.get('question_id')
        choice_id = request.POST.get('choice_id')
        question = get_object_or_404(Poll, pk=question_id)
        choice = get_object_or_404(Choice, pk=choice_id)

        if choice.voters.filter(id=request.user.id).exists():
            context = self.get_context_data(voted=True)
            return self.render_to_response(context)

        choice.votes += 1
        choice.voters.add(request.user)
        choice.save()

        context = self.get_context_data(poll=question)
        return self.render_to_response(context)
