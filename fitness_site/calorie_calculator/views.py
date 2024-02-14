from django.shortcuts import render
from utils import DataMixin
from .models import *
from .forms import *
from . import services
from posts.models import *


mixin = DataMixin()

def home(request):
    global mixin
    

    if request.method == 'POST':
        form = CalculateCalories(request.POST)
        if form.is_valid():
            
            data = form.cleaned_data

            calories = services.get_calories(data['gender'], data['weight'], data['height'], data['age'], data['target'], data['activity_level']) 
            context = mixin.get_user_context(title='Калькулятор калорий', calories=calories, form=form)

            return render(request, 'calorie_calculator/result.html', context=context)

    else:
        form = CalculateCalories()
        context = mixin.get_user_context(title='Калькулятор калорий', form=form)
        return render(request, 'calorie_calculator/index.html', context=context)



def about(request):
    global mixin
    context = mixin.get_user_context(title='О сайте')
    
    return render(request, 'calorie_calculator/about.html', context=context)

