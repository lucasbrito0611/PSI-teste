from django.urls import path
from loja.views.ProdutoView import delete_produto_postback, delete_produto_view, details_produto_view, edit_produto_postback, edit_produto_view, list_produto_view

urlpatterns = [
    path('', list_produto_view, name='produto'),
    path('<int:id>', list_produto_view, name='produto'),
    path('edit/<int:id>', edit_produto_view, name='edit_produto'),
    path('edit', edit_produto_postback, name='edit_produto_postback'),
    path('details/<int:id>', details_produto_view, name='details_produto'),
    path('delete/<int:id>', delete_produto_view, name='delete_produto'),
    path('delete', delete_produto_postback, name='delete_produto_postback')
]