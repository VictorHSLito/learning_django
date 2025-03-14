from django.shortcuts import render
from .models import Topic


def index(request):
    """Retorna a página inicial de learning_logs"""
    return render(request, 'learning_logs/index.html')


def topics(request):
    """Mostra os assuntos"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}

    return render(request, 'learning_logs/topics.html', context)
