from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('loja.urls.HomeUrls')),
    path('', include('loja.urls.AuthUrls')),
    path('produto/', include('loja.urls.ProdutoUrls')),
    path('usuario/', include('loja.urls.UsuarioUrls')),
    path('carrinho/', include('loja.urls.CarrinhoUrls')),
] 

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)