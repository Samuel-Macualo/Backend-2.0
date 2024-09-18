from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import CustomLoginForm
urlpatterns = [
    
    path('', views.register, name='register'),
    path('generar_reporte/', views.generar_reporte, name='generar_reporte'),
    path('home/', views.home, name='home'),

    # Servicio URLs
    path('servicios/', views.servicio_list, name='servicio_list'),
    path('servicio/<int:pk>/', views.servicio_detail, name='servicio_detail'),
    path('servicio/new/', views.servicio_new, name='servicio_new'),
    path('servicio/<int:pk>/edit/', views.servicio_edit, name='servicio_edit'),
    path('servicios/eliminar/<int:pk>/', views.eliminar_servicio, name='eliminar_servicio'),

    # Paquete URLs
    path('paquetes/', views.paquete_list, name='paquete_list'),
    path('paquete/<int:pk>/', views.paquete_detail, name='paquete_detail'),
    path('paquete/new/', views.paquete_new, name='paquete_new'),
    path('paquete/<int:pk>/edit/', views.paquete_edit, name='paquete_edit'),
    path('paquetes/eliminar/<int:pk>/', views.eliminar_paquete, name='eliminar_paquete'),
    
    # Cliente URLs
    path('clientes/', views.cliente_list, name='cliente_list'),
    path('cliente/<int:pk>/', views.cliente_detail, name='cliente_detail'),
    path('cliente/new/', views.cliente_new, name='cliente_new'),
    path('cliente/<int:pk>/edit/', views.cliente_edit, name='cliente_edit'),
    path('clientes/eliminar/<int:pk>/', views.eliminar_cliente, name='eliminar_cliente'),
    
    # Reserva URLs
    path('reservas/', views.reserva_list, name='reserva_list'),
    path('reserva/<int:pk>/', views.reserva_detail, name='reserva_detail'),
    path('reserva/new/', views.reserva_new, name='reserva_new'),
    path('reserva/<int:pk>/edit/', views.reserva_edit, name='reserva_edit'),
    path('reservas/eliminar/<int:pk>/', views.eliminar_reserva, name='eliminar_reserva'),
    

    # Venta URLs
    path('ventas/', views.venta_list, name='venta_list'),
    path('venta/<int:pk>/', views.venta_detail, name='venta_detail'),
    path('venta/new/', views.venta_new, name='venta_new'),
    path('venta/<int:pk>/edit/', views.venta_edit, name='venta_edit'),
    path('ventas/eliminar/<int:pk>/', views.eliminar_venta, name='eliminar_venta'),
    
    
    # Foto URLs
    path('fotos/', views.foto_list, name='foto_list'),
    path('foto/<int:pk>/', views.foto_detail, name='foto_detail'),
    path('foto/new/', views.foto_new, name='foto_new'),
    path('foto/<int:pk>/edit/', views.foto_edit, name='foto_edit'),
    path('fotos/eliminar/<int:pk>/', views.eliminar_foto, name='eliminar_foto'),
    

    # Login URLs
    path('login/', auth_views.LoginView.as_view(
        template_name='registration/login.html',
        authentication_form=CustomLoginForm
    ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    #Recuperar contraseña
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html'), name='password_reset'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
    
]


