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


def topic(request, topic_id):
    """Mostra sobre um assuto em específico"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('data_added')
    context = {'topic': topic, 'entries': entries}

    return render(request, 'learning_logs/topic.html', context)
