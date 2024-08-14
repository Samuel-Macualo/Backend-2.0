from django.shortcuts import render, get_object_or_404, redirect
from .models import Servicio, Paquete, Cliente, Reserva, Venta, Foto
from .forms import ServicioForm, PaqueteForm, ClienteForm, ReservaForm, VentaForm, FotoForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.urls import reverse
from django.views.decorators.cache import never_cache
from django.db.models import Q
from django.http import HttpResponse
from django.apps import apps

@never_cache
@login_required
def generar_reporte(request):
    modulo = request.GET.get('modulo')
    
    if modulo:
        # Limpiamos el valor de 'modulo' para remover posibles '/' al inicio o al final
        modulo = modulo.strip('/').capitalize()  # Eliminamos '/' y capitalizamos la primera letra
        
        try:
            # Imprimimos el nombre del modelo que Django intentará cargar
            print(f"Intentando cargar el modelo: {modulo}")
            
            # Obtenemos el modelo dinámicamente
            Model = apps.get_model('love_story', modulo)
            
            # Obteniendo todos los objetos del modelo
            objetos = Model.objects.all()

            # Renderizando la plantilla con los objetos obtenidos
            return render(request, 'generar_reportes.html', {'objetos': objetos})

        except LookupError:
            return HttpResponse("Módulo no encontrado")
    else:
        return HttpResponse("No se especificó ningún módulo")

    
  
@never_cache
@login_required
def home(request):
    return render(request, 'home.html')

# Servicio views
@never_cache
@login_required
def servicio_list(request):
    servicios = Servicio.objects.all()
    return render(request, 'servicio/servicio_list.html', {'servicios': servicios})

@never_cache
@login_required
def servicio_detail(request, pk):
    servicio = get_object_or_404(Servicio, pk=pk)
    return render(request, 'servicio/servicio_detail.html', {'servicio': servicio})

@never_cache
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

@never_cache
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
@never_cache
@login_required
def paquete_list(request):
    paquetes_list = Paquete.objects.all()
    paginator = Paginator(paquetes_list, 10)  # Muestra 10 paquetes por página
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'paquete/paquete_list.html', {'page_obj': page_obj})

@never_cache
@login_required
def paquete_list(request):
    query = request.GET.get('query')
    column = request.GET.get('column')
    paquetes = Paquete.objects.all()

    if query and column:
        if column == 'id':
            paquetes = paquetes.filter(id__icontains=query)
        elif column == 'nombre_paquete':
            paquetes = paquetes.filter(nombre_paquete__icontains=query)
        elif column == 'descripcion':
            paquetes = paquetes.filter(descripcion__icontains=query)
        elif column == 'precio':
            paquetes = paquetes.filter(precio__icontains=query)

    paginator = Paginator(paquetes, 10)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)
    return render(request, 'paquete/paquete_list.html', {'page_obj': page_obj})

@never_cache
@login_required
def paquete_detail(request, pk):
    paquete = get_object_or_404(Paquete, pk=pk)
    return render(request, 'paquete/paquete_detail.html', {'paquete': paquete})

@never_cache
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

@never_cache
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

@never_cache
@login_required
def eliminar_paquete(request, pk):
    paquete = get_object_or_404(Paquete, pk=pk)
    paquete.delete()
    return redirect(reverse('paquete_list'))

# Cliente views
@never_cache
@login_required
def cliente_list(request):
    clientes = Cliente.objects.all()
    return render(request, 'cliente/cliente_list.html', {'clientes': clientes})

@never_cache
@login_required
def cliente_detail(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    return render(request, 'cliente/cliente_detail.html', {'cliente': cliente})

@never_cache
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

@never_cache
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
@never_cache
@login_required
def reserva_list(request):
    reservas = Reserva.objects.all()
    return render(request, 'reserva/reserva_list.html', {'reservas': reservas})

@never_cache
@login_required
def reserva_detail(request, pk):
    reserva = get_object_or_404(Reserva, pk=pk)
    return render(request, 'reserva/reserva_detail.html', {'reserva': reserva})

@never_cache
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

@never_cache
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
@never_cache
@login_required
def venta_list(request):
    ventas = Venta.objects.all()
    return render(request, 'venta/venta_list.html', {'ventas': ventas})

@never_cache
@login_required
def venta_detail(request, pk):
    venta = get_object_or_404(Venta, pk=pk)
    return render(request, 'venta/venta_detail.html', {'venta': venta})

@never_cache
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

@never_cache
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
@never_cache
@login_required
def foto_list(request):
    fotos = Foto.objects.all()
    return render(request, 'foto/foto_list.html', {'fotos': fotos})

@never_cache
@login_required
def foto_detail(request, pk):
    foto = get_object_or_404(Foto, pk=pk)
    return render(request, 'foto/foto_detail.html', {'foto': foto})

@never_cache
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

@never_cache
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
