from django import forms
from .models import *
from django.utils.text import slugify
from unidecode import unidecode


class AddPageForm(forms.ModelForm):

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = 'Выберите категорию'

    class Meta:
        model = Posts
        fields = ['title', 'content', 'description', 'cat', 'photo']
        widgets = {
            'title': forms.TextInput({'class': 'form-control'}),
            'content': forms.Textarea({'class': 'form-control', 'rows': '5'}),
            'description': forms.TextInput({'class': 'form-control'}),
            'cat': forms.Select({'class': 'form-select'}),
            'photo': forms.ClearableFileInput({'class': 'form-control'})
        }

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        if title:
            slug = slugify(unidecode(title))  # Создание slug на основе title с преобразованием русских символов
            cleaned_data['slug'] = slug  # Установка значения slug в поле формы

        return cleaned_data  # Возвращаем очищенные данные
    


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4, 'class': 'form-control', 'name': 'content', 'placeholder': 'Напишите свой комментарий сюда :)'})
        }


