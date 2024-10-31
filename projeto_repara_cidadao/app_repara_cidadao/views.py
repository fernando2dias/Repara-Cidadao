from lib2to3.fixes.fix_input import context

from django.shortcuts import render, redirect

from .models import Usuario, Reparo  # Importação mais concisa
from .forms import ReparoModelForm

def home (request):
    return render (request, 'home.html')


def cadastro(request):
    return render(request, 'usuarios/cadastro.html')


def usuarios(request):
    # Salvar os dados da tela para o banco de dados.
    if request.method == 'POST':
        novo_usuario = Usuario()
        novo_usuario.nome = request.POST.get('nome')
        novo_usuario.sobrenome = request.POST.get('sobrenome')
        novo_usuario.data_nascimento = request.POST.get('data_nascimento')
        novo_usuario.telefone = request.POST.get('telefone')
        novo_usuario.email = request.POST.get('email')
        novo_usuario.cpf = request.POST.get('cpf')
        novo_usuario.rua = request.POST.get('rua')
        novo_usuario.numero = request.POST.get('numero')
        novo_usuario.bairro = request.POST.get('bairro')
        novo_usuario.cidade = request.POST.get('cidade')
        novo_usuario.estado = request.POST.get('estado')
        novo_usuario.cep = request.POST.get('cep')
        novo_usuario.save()


    # Exibir todos os usuários já cadastrados em uma nova página 
    usuarios = {
        'usuarios': Usuario.objects.all()
    }
    
    return render(request, 'usuarios/usuarios.html', usuarios)

def cadastro_reparo(request):
    return render(request, 'reparos/cadastro-reparo.html')


def lista_reparos(request):
    if request.method == 'POST':
        form = ReparoModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_reparos')
    else:
        form = ReparoModelForm()

    reparos = {
        'reparos': Reparo.objects.all(),
    }
    return render(request, 'reparos/lista_reparos.html', reparos)


