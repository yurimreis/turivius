from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from message_turivius.api.viewsets import MessageViewSet

# Criação das rotas
router = routers.DefaultRouter()
# Registro de uma rota chamada message que recebe uma viewset como parâmetro
router.register(r'message', MessageViewSet)

# Rotas do Django
urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
