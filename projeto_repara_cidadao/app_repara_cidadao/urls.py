from django.urls import path
from .views import home, cadastro, usuarios, formulario_reparos, lista_reparos


urlpatterns = [
    # rota, view responsável, nome de referência
    path('', home, name='home'),
    path('cadastro', cadastro, name='cadastro'),
    path('usuarios/', usuarios, name='listagem_usuarios'),
    path('reparos/', formulario_reparos, name='formulario_reparos'),
    path('listagem-reparos/', lista_reparos, name='listagem_reparos')
]