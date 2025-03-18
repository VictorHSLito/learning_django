from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.urls import reverse


def logout_view(request):
    """Faz o logout do usuário"""
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))
