from django.contrib import admin
from .models import * 

# Register your models here.

class FabricanteAdmin(admin.ModelAdmin):
    date_hierarchy = 'criado_em'

class ProdutoAdmin(admin.ModelAdmin):
    date_hierarchy = 'criado_em'
    list_display = ('Produto', 'destaque', 'promocao', 'msgPromocao', 'preco', 'categoria',)
    empty_value_display = 'Vazio'

admin.site.register(Fabricante, FabricanteAdmin) 
admin.site.register(Categoria)
admin.site.register(Produto, ProdutoAdmin)