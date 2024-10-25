from django.shortcuts import render
from .models import Usuario, Reparo  # Importação mais concisa


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


def formulario_reparos(request):
    return render(request, 'reparos/reparos.html')


def lista_reparos(request):
    # Salvar os dados da tela para o banco de dados.
    if request.method == 'POST':
        novo_reparo = Reparo()
        novo_reparo.reparo = request.POST.get('reparo')
        novo_reparo.rua = request.POST.get('rua')
        novo_reparo.numero = request.POST.get('numero')
        novo_reparo.bairro = request.POST.get('bairro')
        novo_reparo.cidade = request.POST.get('cidade')
        novo_reparo.estado = request.POST.get('estado')
        novo_reparo.cep = request.POST.get('cep')
        novo_reparo.save()

    # Exibir todos os reparos cadastrados
    listagem_reparos = {
        'reparos': Reparo.objects.all()
    }
    
    return render(request, 'reparos/lista_reparos.html', listagem_reparos)

