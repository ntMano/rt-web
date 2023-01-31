from django.shortcuts import render
from django.http import HttpResponse
from .models import SolicitaRT
from itertools import cycle

# Create your views here.


LENGTH_CNPJ = 14


def is_cnpj_valido(cnpj: str) -> bool:
    if len(cnpj) != LENGTH_CNPJ:
        return False

    if cnpj in (c * LENGTH_CNPJ for c in "1234567890"):
        return False

    cnpj_r = cnpj[::-1]
    for i in range(2, 0, -1):
        cnpj_enum = zip(cycle(range(2, 10)), cnpj_r[i:])
        dv = sum(map(lambda x: int(x[1]) * x[0], cnpj_enum)) * 10 % 11
        if cnpj_r[i - 1:i] != str(dv % 10):
            return False

    return True


def rts(request):
    if request.method == "GET":
        return render(request, 'rts.html')
    elif request.method == "POST":
        ano = request.POST.get('ano')
        parecer = request.POST.get('parecer')
        situacao = request.POST.get('situacao')
        pj = request.POST.get('pj')
        instituicao = request.POST.get('instituicao')
        cnpj = request.POST.get('cnpj')
        municipio = request.POST.get('municipio')
        data_solicitacao = request.POST.get('data_solicitacao')
        tipo_solicitacao = request.POST.get('tipo_solicitacao')
        nome_rt = request.POST.get('nome_rt')
        rt_tel = request.POST.get('rt_tel')
        rt_email = request.POST.get('rt_email')
        data_enc_presidencia = request.POST.get('data_enc_presidencia')
        data_rec_presidencia = request.POST.get('data_rec_presidencia')
        numero_art = request.POST.get('numero_art')
        livro = request.POST.get('livro')
        folha = request.POST.get('folha')
        data_homologacao = request.POST.get('data_homologacao')
        data_validade = request.POST.get('data_validade')

        solicita_rt = SolicitaRT(
            ano=ano,
            parecer=parecer,
            situacao=situacao,
            pj=pj,
            instituicao=instituicao,
            cnpj=cnpj,
            municipio=municipio,
            data_solicitacao=data_solicitacao,
            tipo_solicitacao=tipo_solicitacao,
            nome_rt=nome_rt,
            rt_tel=rt_tel,
            rt_email=rt_email,
            data_enc_presidencia=data_enc_presidencia,
            data_rec_presidencia=data_rec_presidencia,
            numero_art=numero_art,
            livro=livro,
            folha=folha,
            data_homologacao=data_homologacao,
            data_validade=data_validade,
        )

        # if not re.fullmatch(re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'), rt_email):

        #     return render(request, 'rts.html', {'ano': ano, 'parecer': parecer, 'situacao': situacao, 'pj': pj, 'instituicao': instituicao, 'cnpj': cnpj, 'municipio': municipio, 'data_solicitacao': data_solicitacao, 'tipo_solicitaca': tipo_solicitacao, 'nome_rt': nome_rt, 'rt_tel': rt_tel, 'data_enc_presidencia': data_enc_presidencia, 'data_rec_presidencia': data_rec_presidencia, 'numero_art': numero_art, 'livro': livro, 'folha': folha, 'data_homologacao': data_homologacao, 'data_validade': data_validade})

        is_cnpj_valido(cnpj)

        if not is_cnpj_valido(cnpj):

            return render(request, 'rts.html', {'ano': ano, 'parecer': parecer, 'situacao': situacao, 'pj': pj, 'instituicao': instituicao, 'rt_email': rt_email, 'municipio': municipio, 'data_solicitacao': data_solicitacao, 'tipo_solicitaca': tipo_solicitacao, 'nome_rt': nome_rt, 'rt_tel': rt_tel, 'data_enc_presidencia': data_enc_presidencia, 'data_rec_presidencia': data_rec_presidencia, 'numero_art': numero_art, 'livro': livro, 'folha': folha, 'data_homologacao': data_homologacao, 'data_validade': data_validade})

        solicita_rt.save()

    return HttpResponse('teste')
