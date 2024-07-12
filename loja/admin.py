from django.contrib import admin
from .models import * 

# Register your models here.

class FabricanteAdmin(admin.ModelAdmin):
    date_hierarchy = 'criado_em'
    search_fields = ('Fabricante',)

class CategoriaAdmin(admin.ModelAdmin):
    date_hierarchy = 'criado_em'
    search_fields = ('Categoria',)

class ProdutoAdmin(admin.ModelAdmin):
    date_hierarchy = 'criado_em'
    list_display = ('Produto', 'destaque', 'promocao', 'msgPromocao', 'preco', 'categoria',)
    empty_value_display = 'Vazio'
    search_fields = ('Produto',)

admin.site.register(Fabricante, FabricanteAdmin) 
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Produto, ProdutoAdmin)