from django.urls import path
from app_repara_cidadao import views

urlpatterns = [
    # rota, view responsável, nome de referência
    path('cadastro', views.cadastro, name='cadastro'),
    path('usuarios/', views.usuarios, name='listagem_usuarios'),
    path('reparos/', views.formulario_reparos, name='formulario_reparos'),
    path('listagem-reparos/', views.lista_reparos, name='listagem_reparos')
]
