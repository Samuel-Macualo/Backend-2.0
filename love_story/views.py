from django.shortcuts import render, get_object_or_404, redirect
from .models import Servicio, Paquete, Cliente, Reserva, Venta, Foto
from .forms import ServicioForm, PaqueteForm, ClienteForm, ReservaForm, VentaForm, FotoForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.urls import reverse

@login_required
def home(request):
    return render(request, 'home.html')

# Servicio views
@login_required
def servicio_list(request):
    servicios = Servicio.objects.all()
    return render(request, 'servicio/servicio_list.html', {'servicios': servicios})

@login_required
def servicio_detail(request, pk):
    servicio = get_object_or_404(Servicio, pk=pk)
    return render(request, 'servicio/servicio_detail.html', {'servicio': servicio})

@login_required
def servicio_new(request):
    if request.method == "POST":
        form = ServicioForm(request.POST)
        if form.is_valid():
            servicio = form.save()
            return redirect('servicio/servicio_detail', pk=servicio.pk)
    else:
        form = ServicioForm()
    return render(request, 'servicio/servicio_edit.html', {'form': form})

@login_required
def servicio_edit(request, pk):
    servicio = get_object_or_404(Servicio, pk=pk)
    if request.method == "POST":
        form = ServicioForm(request.POST, instance=servicio)
        if form.is_valid():
            servicio = form.save()
            return redirect('servicio/servicio_detail', pk=servicio.pk)
    else:
        form = ServicioForm(instance=servicio)
    return render(request, 'servicio/servicio_edit.html', {'form': form})

# Paquete views
@login_required
def paquete_list(request):
    paquetes_list = Paquete.objects.all()
    paginator = Paginator(paquetes_list, 10)  # Muestra 10 paquetes por página
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'paquete/paquete_list.html', {'page_obj': page_obj})


@login_required
def paquete_detail(request, pk):
    paquete = get_object_or_404(Paquete, pk=pk)
    return render(request, 'paquete/paquete_detail.html', {'paquete': paquete})

@login_required
def paquete_new(request):
    if request.method == "POST":
        form = PaqueteForm(request.POST)
        if form.is_valid():
            paquete = form.save()
            return redirect('paquete_list')
    else:
        form = PaqueteForm()
    return render(request, 'paquete/paquete_form.html', {'form': form})

@login_required
def paquete_edit(request, pk):
    paquete = get_object_or_404(Paquete, pk=pk)
    if request.method == "POST":
        form = PaqueteForm(request.POST, instance=paquete)
        if form.is_valid():
            paquete = form.save()
            return redirect('paquete_detail', pk=paquete.pk)
    else:
        form = PaqueteForm(instance=paquete)
    return render(request, 'paquete/paquete_form.html', {'form': form})

@login_required
def eliminar_paquete(request, pk):
    paquete = get_object_or_404(Paquete, pk=pk)
    paquete.delete()
    return redirect(reverse('paquete_list'))

# Cliente views
@login_required
def cliente_list(request):
    clientes = Cliente.objects.all()
    return render(request, 'cliente/cliente_list.html', {'clientes': clientes})

@login_required
def cliente_detail(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    return render(request, 'cliente/cliente_detail.html', {'cliente': cliente})

@login_required
def cliente_new(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save()
            return redirect('cliente/cliente_detail', pk=cliente.pk)
    else:
        form = ClienteForm()
    return render(request, 'cliente/cliente_edit.html', {'form': form})

@login_required
def cliente_edit(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == "POST":
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            cliente = form.save()
            return redirect('cliente/cliente_detail', pk=cliente.pk)
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'cliente/cliente_edit.html', {'form': form})

# Reserva views
@login_required
def reserva_list(request):
    reservas = Reserva.objects.all()
    return render(request, 'reserva/reserva_list.html', {'reservas': reservas})

@login_required
def reserva_detail(request, pk):
    reserva = get_object_or_404(Reserva, pk=pk)
    return render(request, 'reserva/reserva_detail.html', {'reserva': reserva})

@login_required
def reserva_new(request):
    if request.method == "POST":
        form = ReservaForm(request.POST)
        if form.is_valid():
            reserva = form.save()
            return redirect('reserva/reserva_detail', pk=reserva.pk)
    else:
        form = ReservaForm()
    return render(request, 'reserva/reserva_edit.html', {'form': form})

@login_required
def reserva_edit(request, pk):
    reserva = get_object_or_404(Reserva, pk=pk)
    if request.method == "POST":
        form = ReservaForm(request.POST, instance=reserva)
        if form.is_valid():
            reserva = form.save()
            return redirect('reserva/reserva_detail', pk=reserva.pk)
    else:
        form = ReservaForm(instance=reserva)
    return render(request, 'reserva/reserva_edit.html', {'form': form})

# Venta views
@login_required
def venta_list(request):
    ventas = Venta.objects.all()
    return render(request, 'venta/venta_list.html', {'ventas': ventas})

@login_required
def venta_detail(request, pk):
    venta = get_object_or_404(Venta, pk=pk)
    return render(request, 'venta/venta_detail.html', {'venta': venta})

@login_required
def venta_new(request):
    if request.method == "POST":
        form = VentaForm(request.POST)
        if form.is_valid():
            venta = form.save()
            return redirect('venta/venta_detail', pk=venta.pk)
    else:
        form = VentaForm()
    return render(request, 'venta/venta_edit.html', {'form': form})

@login_required
def venta_edit(request, pk):
    venta = get_object_or_404(Venta, pk=pk)
    if request.method == "POST":
        form = VentaForm(request.POST, instance=venta)
        if form.is_valid():
            venta = form.save()
            return redirect('venta/venta_detail', pk=venta.pk)
    else:
        form = VentaForm(instance=venta)
    return render(request, 'venta/venta_edit.html', {'form': form})

# Foto views
@login_required
def foto_list(request):
    fotos = Foto.objects.all()
    return render(request, 'foto/foto_list.html', {'fotos': fotos})

@login_required
def foto_detail(request, pk):
    foto = get_object_or_404(Foto, pk=pk)
    return render(request, 'foto/foto_detail.html', {'foto': foto})

@login_required
def foto_new(request):
    if request.method == "POST":
        form = FotoForm(request.POST)
        if form.is_valid():
            foto = form.save()
            return redirect('foto/foto_detail', pk=foto.pk)
    else:
        form = FotoForm()
    return render(request, 'foto/foto_edit.html', {'form': form})

@login_required
def foto_edit(request, pk):
    foto = get_object_or_404(Foto, pk=pk)
    if request.method == "POST":
        form = FotoForm(request.POST, instance=foto)
        if form.is_valid():
            foto = form.save()
            return redirect('foto/foto_detail', pk=foto.pk)
    else:
        form = FotoForm(instance=foto)
    return render(request, 'fotofoto_edit.html', {'form': form})

# Create your views here.
