from django.db import models


# Criação da classe onde é definido os campos para cadastro
class MessageTurivius(models.Model):
    title = models.CharField(max_length=100, null=False)
    text = models.TextField(null=False)

    # Retorna o título da mensagem como visualização para o usuário
    def __str__(self):
        return self.title