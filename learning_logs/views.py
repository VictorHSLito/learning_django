from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Topic
from .forms import TopicForm, EntryForm


def index(request):
    """Função para criar a view da página incial 'learning_logs'"""
    return render(request, 'learning_logs/index.html')


def topics(request):
    """Função para criar a view de todos os assuntos"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}

    return render(request, 'learning_logs/topics.html', context)


def topic(request, topic_id):
    """Função para criar a view sobre um assuto em específico"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('data_added')
    context = {'topic': topic, 'entries': entries}

    return render(request, 'learning_logs/topic.html', context)


def new_topic(request):
    """Função para criar a view para adicionar um novo assunto"""
    if request.method != 'POST':  # Se nenhum dado foi enviado, cria um formulário em branco
        form = TopicForm()
    else:
        form = TopicForm(request.POST)
        if form.is_valid():  # Verifica se todas as informações contidas no formulário são válidas
            form.save()  # Salva os dados do formulário no banco de dados
            return HttpResponseRedirect(reverse('learning_logs:topics'))  # Redireciona o usuário para a página de topics

    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)


def new_entry(request, topic_id):
    """Função para criar a view para adicionar uma nova entrada"""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic_id]))

    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)
