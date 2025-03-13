from django.shortcuts import render

def index(request):
    """Retorna a página inicial de learning_logs"""
    return render(request, 'learning_logs/index.html')
