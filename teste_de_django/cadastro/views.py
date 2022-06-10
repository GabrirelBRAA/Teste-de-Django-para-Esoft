from django.shortcuts import render, redirect
from django.http import HttpRequest
from .models import Cadastro
# Create your views here.

def tela_inicial(request):
    dados=Cadastro.objects.all()
    return render(request, 'cadastro/intro_template.html', {'dados':dados})

def post(request):
    return render(request, 'cadastro/tela_de_cadastro.html')

def registrar(request):
    if request.method=='POST':
        dados=request.POST.dict()

    else:
        pass #Colocar retorno ao registro aqui com mensagem de erro

    keys=["cep", "endereco", "numero", "complemento", "bairro", "cidade", "uf", "descricao"]
    dados_uteis={x:dados[x] for x in keys}
    query=Cadastro.objects.filter(cep=dados_uteis["cep"]).first()  #Busca elemento com mesmo CEP e, se achar, o atualiza
    if query:
        for key, value in dados_uteis.items():
            if value:
                setattr(query,key, value)

        query.save()

    else:  # Se não achar cria um novo elemento
        novo_registro= Cadastro.objects.create(**dados_uteis)
        novo_registro.save()

    return redirect('/')

