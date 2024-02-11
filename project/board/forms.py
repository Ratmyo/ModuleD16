from django import forms
from django.core.exceptions import ValidationError
from .models import Article, UserResponse

class ArticleForm(forms.ModelForm):
    title = forms.CharField(min_length=10)

    class Meta:
        model = Article
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        text = cleaned_data.get('text')
        title = cleaned_data.get('title')

        if title == text:
            raise ValidationError(
                'Описание не должно быть идентично названию.'
            )

        return cleaned_data


class ResponseForm(forms.ModelForm):
    class Meta:
        model = UserResponse
        fields = ['text']
        labels = ['Response']
