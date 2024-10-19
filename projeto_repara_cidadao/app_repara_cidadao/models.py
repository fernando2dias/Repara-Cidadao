from django.db import models

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255, null=False, blank= True)
    sobrenome = models.CharField(max_length=100, null=False, blank= True)
    cpf = models.CharField(max_length=14, unique=True, null=True, blank= False)
    data_nascimento = models.DateField(null=True, blank= True)
    email = models.EmailField(null=True, blank= True)
    telefone = models.CharField(max_length=15, null=True, blank= True)
    rua = models.CharField(max_length=255, null=True, blank= True)
    numero = models.CharField(max_length=10, null=True, blank= True)
    complemento = models.CharField(max_length=255, blank = True)
    bairro = models.CharField(max_length=100, null=True, blank= True)
    cidade = models.CharField(max_length=100, null=True, blank= True, default='Sorocaba')
    estado = models.CharField(max_length=100, default='São Paulo')
    cep = models.CharField(max_length=10, null=True, blank= True, default = '00000-000')
    referencia = models.CharField(max_length=255, blank = True)
    
       
    def __str__(self):
        return "{self.nome} {self.idade}"
