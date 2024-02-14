from django import forms


class CalculateCalories(forms.Form):
    GENDER_CHOICES = (
        ('M', 'Мужской'),
        ('Ж', 'Женский')
    )

    ACTIVITY_LEVEL = (
        ('минимальный', 'Сидячая работа, отсутствие физических нагрузок'),
        ('низкий', 'Тренировки не менее 20 мин 1-3 раза в неделю'),
        ('умеренный', 'Тренировки 30-60 мин 3-4 раза в неделю'),
        ('высокий', 'Тренировки 30-60 мин 5-7 раза в неделю; тяжелая физическая работа'),
        ('экстремальный', 'Несколько интенсивных тренировок в день 6-7 раз в неделю; очень трудоемкая работа')
    )

    TARGETS = (
        ('Похудение', 'Похудение'),
        ('Поддержание', 'Поддержание нынешнего веса'),
        ('Набор', 'Набор веса')
    )

    gender = forms.ChoiceField(choices=GENDER_CHOICES, label='Пол', widget=forms.RadioSelect(attrs={'class': ''}))
    age = forms.IntegerField(label='Возраст', widget=forms.NumberInput(attrs={'class': 'custom-form-control', 'placeholder': 'Возраст', 'min': '1', 'max': '120'}))
    height = forms.IntegerField(label='Рост', widget=forms.NumberInput(attrs={'class': 'custom-form-control', 'placeholder': 'см', 'min': '1', 'max': '250'}))
    weight = forms.IntegerField(label='Вес', widget=forms.NumberInput(attrs={'class': 'custom-form-control', 'placeholder': 'кг', 'min': '1', 'max': '250'}))
    activity_level = forms.ChoiceField(choices=ACTIVITY_LEVEL, 
                                       label='Уровень активности', widget=forms.RadioSelect())
    target = forms.ChoiceField(choices=TARGETS,
                               label='Цель', widget=forms.RadioSelect())