from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import CustomLoginForm
urlpatterns = [
    path('', views.home, name='home'),
    # Servicio URLs
    path('servicios/', views.servicio_list, name='servicio_list'),
    path('servicio/<int:pk>/', views.servicio_detail, name='servicio_detail'),
    path('servicio/new/', views.servicio_new, name='servicio_new'),
    path('servicio/<int:pk>/edit/', views.servicio_edit, name='servicio_edit'),
    
    # Paquete URLs
    path('paquetes/', views.paquete_list, name='paquete_list'),
    path('paquete/<int:pk>/', views.paquete_detail, name='paquete_detail'),
    path('paquete/new/', views.paquete_new, name='paquete_new'),
    path('paquete/<int:pk>/edit/', views.paquete_edit, name='paquete_edit'),
    
    # Cliente URLs
    path('clientes/', views.cliente_list, name='cliente_list'),
    path('cliente/<int:pk>/', views.cliente_detail, name='cliente_detail'),
    path('cliente/new/', views.cliente_new, name='cliente_new'),
    path('cliente/<int:pk>/edit/', views.cliente_edit, name='cliente_edit'),
    
    # Reserva URLs
    path('reservas/', views.reserva_list, name='reserva_list'),
    path('reserva/<int:pk>/', views.reserva_detail, name='reserva_detail'),
    path('reserva/new/', views.reserva_new, name='reserva_new'),
    path('reserva/<int:pk>/edit/', views.reserva_edit, name='reserva_edit'),
    
    # Venta URLs
    path('ventas/', views.venta_list, name='venta_list'),
    path('venta/<int:pk>/', views.venta_detail, name='venta_detail'),
    path('venta/new/', views.venta_new, name='venta_new'),
    path('venta/<int:pk>/edit/', views.venta_edit, name='venta_edit'),
    
    # Foto URLs
    path('fotos/', views.foto_list, name='foto_list'),
    path('foto/<int:pk>/', views.foto_detail, name='foto_detail'),
    path('foto/new/', views.foto_new, name='foto_new'),
    path('foto/<int:pk>/edit/', views.foto_edit, name='foto_edit'),

    # Login URLs
    path('accounts/login/', auth_views.LoginView.as_view(
        template_name='registration/login.html',
        authentication_form=CustomLoginForm
    ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]


