from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse

from .models import Topic, Entry
from .forms import TopicForm, EntryForm


def index(request):
    """Função para criar a view da página incial 'learning_logs'"""
    return render(request, 'learning_logs/index.html')


@login_required
def topics(request):
    """Função para criar a view de todos os assuntos"""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}

    return render(request, 'learning_logs/topics.html', context)


@login_required
def topic(request, topic_id):
    """Função para criar a view sobre um assuto em específico"""
    topic = Topic.objects.get(id=topic_id)
    if topic.owner != request.user:
        raise Http404
    entries = topic.entry_set.order_by('data_added')
    context = {'topic': topic, 'entries': entries}

    return render(request, 'learning_logs/topic.html', context)


@login_required
def new_topic(request):
    """Função para criar a view para adicionar um novo assunto"""
    if request.method != 'POST':  # Se nenhum dado foi enviado, cria um formulário em branco
        form = TopicForm()
    else:
        form = TopicForm(request.POST)
        if form.is_valid():  # Verifica se todas as informações contidas no formulário são válidas
            new_topic = form.save(commit=False)  # Salva previamente as informações contidas no formulário
            new_topic.owner = request.user  # Associa esse novo tópico ao usuário do request
            new_topic.save()  # Por fim, salva essas informações no banco
            return HttpResponseRedirect(
                reverse('learning_logs:topics'))  # Redireciona o usuário para a página de topics

    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)


@login_required
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


@login_required
def edit_entry(request, entry_id):
    """Função para criar a view para editar uma entrada existente"""
    entry = Entry.objects.get(id=entry_id)
    print(entry_id)
    topic = entry.topic

    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic.id]))

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)
