from django import forms
from .models import Topic, Entry


class TopicForm(forms.ModelForm):  # Usa uma classe própria do Django feita exclusivamente para formulários
    class Meta:
        """Essa classe informa ao Django sobre qual classe ele deve basear-se a criação do formulário"""
        model = Topic
        fields = ['text']
        labels = {"text": ""}


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        # forms.Textarea personaliza o widget para uma TextArea, com um tamanho de 80 colunas
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}  # É um elemento de formulário do HTML

