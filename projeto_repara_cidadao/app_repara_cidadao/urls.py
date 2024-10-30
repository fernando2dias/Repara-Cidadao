from django.urls import path
from .views import home, cadastro, usuarios, cadastro_reparo, lista_reparos

urlpatterns = [
    # rota, view responsável, nome de referência
    path('', home, name='home'),
    path('cadastro/', cadastro, name='cadastro'),
    path('usuarios/', usuarios, name='listagem_usuarios'),
    path('cadastro-reparo/', cadastro_reparo, name='cadastro_reparo'),
    path('lista-reparos/', lista_reparos, name='lista_reparos')
]