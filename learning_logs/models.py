from django.db import models


class Topic(models.Model):
    """"Classe que representa os tópicos que o usuário
    está estudando"""
    text = models.CharField(max_length=150)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Devolve uma representação em string do modelo"""
        return self.text


class Entry(models.Model):
    """"Classe para representar alggo específico
    aprendido sobre um assunto"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    data_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        """"A classe Meta serve para fornecer informações adicionais que
        controlam aspectos de como o modelo se comporta ou é tratado pelo Django,
         como o nome plural da tabela, a ordem de exibição de objetos, permissões,
         entre outras configurações."""
        verbose_name_plural = 'entries'

        def __str__(self):
            """"Devolve um representação em string do modelo"""
            return self.text[:50] + "..."

