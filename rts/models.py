from django.db import models
import re
from django.http import HttpResponse

# Create your models here.






class SolicitaRT(models.Model):
    ano = models.CharField(max_length=4)
    parecer = models.CharField(max_length=4)
    situacao = models.CharField(max_length=80)
    pj = models.CharField(max_length=80)
    instituicao = models.CharField(max_length=200)
    cnpj = models.CharField(max_length=14)
    municipio = models.CharField(max_length=80)
    data_solicitacao = models.CharField(max_length=80)
    tipo_solicitacao = models.CharField(max_length=80)
    nome_rt = models.CharField(max_length=80)
    rt_tel = models.CharField(max_length=11)
    rt_email = models.EmailField(max_length=100)
    data_enc_presidencia = models.CharField(max_length=10)
    data_rec_presidencia = models.CharField(max_length=10)
    numero_art = models.CharField(max_length=4)
    livro = models.CharField(max_length=3)
    folha = models.CharField(max_length=4)
    data_homologacao = models.CharField(max_length=10)
    data_validade = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.nome_rt
