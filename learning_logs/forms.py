from django import forms
from .models import Topic


class TopicForm(forms.ModelForm):  # Usa uma classe própria do Django feita exclusivamente para formulários
    class Meta:
        """Essa classe informa ao Django sobre qual classe ele deve basear-se a criação do formulário"""
        model = Topic
        fields = ['text']
        labels = {"text": ""}


