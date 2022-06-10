from django.urls import path
from . import views

app_name = 'cadastro'
urlpatterns = [
    path('', views.tela_inicial),
    path('post/', views.post ,name='post'),
    path('registrar/', views.registrar, name="registrar"),
]