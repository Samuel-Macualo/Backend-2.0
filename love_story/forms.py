from django import forms
from .models import Servicio, Paquete, Cliente, Reserva, Venta, Foto, CustomUser
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 
        'placeholder': 'Nombre de usuario',
        'id': 'username-input'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control', 
        'placeholder': 'Contraseña',
        'id': 'password-input'
    }))

class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = ['tipo_de_servicio', 'descripcion', 'precio_base']

class PaqueteForm(forms.ModelForm):
    class Meta:
        model = Paquete
        fields = ['nombre_paquete', 'descripcion', 'precio']

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'email', 'telefono', 'direccion']

class ReservaForm(forms.ModelForm):
    fecha_reserva = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'})
    )
    class Meta:
        model = Reserva
        fields = ['fecha_reserva', 'estado', 'cliente', 'servicio']

class VentaForm(forms.ModelForm):
    fecha_venta = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'})
    )
    class Meta:
        model = Venta
        fields = ['fecha_venta', 'total', 'cliente', 'paquete']

class FotoForm(forms.ModelForm):
    class Meta:
        model = Foto
        fields = ['url', 'descripcion', 'reserva']


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone = forms.CharField(required=False)

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'phone', 'password1', 'password2')