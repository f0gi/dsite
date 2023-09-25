from .models import Forms
from django.forms import ModelForm, TextInput, Textarea


class FormsForm(ModelForm):
    class Meta:
        model = Forms
        fields = ['title', 'name', 'age', 'comment']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название анкеты'
            }),
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите имя'
            }),
            "age": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите возраст'
            }),
            "comment": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите комментарий'
            }),

        }