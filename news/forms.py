from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        # fields = '__all__'
        fields = ['title', 'anons', 'full_text', 'date']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Name of post'
            }),
            "anons": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Anons of post'
            }),
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Text of post'
            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Date'
            })
        }
