from django.contrib import admin

from .models import Usuario, Reparo

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'email')

class ReparoAdmin(admin.ModelAdmin):
    list_display = ('reparo', 'rua', 'numero', 'bairro', 'status')

admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Reparo, ReparoAdmin)
