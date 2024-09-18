from django.shortcuts import render, get_object_or_404, redirect
from .models import Servicio, Paquete, Cliente, Reserva, Venta, Foto
from .forms import ServicioForm, PaqueteForm, ClienteForm, ReservaForm, VentaForm, FotoForm, CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.db import transaction
from django.contrib import messages
from django.core.paginator import Paginator
from django.urls import reverse
from django.views.decorators.cache import never_cache
from django.db.models import Q
from django.http import HttpResponse
from django.apps import apps


@transaction.atomic
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Inicia sesión automáticamente
            messages.success(request, f'Bienvenido {user.first_name} a Love Story.')
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


@never_cache
@login_required
def generar_reporte(request):
    modulo = request.GET.get('modulo')
    
    if modulo:
        modulo = modulo.strip('/').capitalize()[:-1]  # Remover la 's' final si existe
        try:
            print(f"Intentando cargar el modelo: {modulo}")
            
            Model = apps.get_model('love_story', modulo)
            objetos = Model.objects.all()

            # Preparar la lista de datos a mostrar en la plantilla
            lista_objetos = []
            for obj in objetos:
                campos = [(field.verbose_name, getattr(obj, field.name)) for field in obj._meta.fields]
                lista_objetos.append(campos)

            return render(request, 'generar_reportes.html', {'lista_objetos': lista_objetos})

        except LookupError:
            print(f"Error: Módulo {modulo} no encontrado en la app 'love_story'.")
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
    query = request.GET.get('query')
    column = request.GET.get('column')
    servicios = Servicio.objects.all()

    if query and column:
        if column == 'id':
            servicios = servicios.filter(id__icontains=query)
        elif column == 'tipo_de_servicio':
            servicios = servicios.filter(tipo_de_servicio__icontains=query)
        elif column == 'descripcion':
            servicios = servicios.filter(descripcion__icontains=query)
        elif column == 'precio_base':
            servicios = servicios.filter(precio_base__icontains=query)

    paginator = Paginator(servicios, 10)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)
    return render(request, 'servicio/servicio_list.html', {'page_obj': page_obj})

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
            return redirect('servicio_list')
    else:
        form = ServicioForm()
    return render(request, 'servicio/servicio_form.html', {'form': form})

@never_cache
@login_required
def servicio_edit(request, pk):
    servicio = get_object_or_404(Servicio, pk=pk)
    if request.method == "POST":
        form = ServicioForm(request.POST, instance=servicio)
        if form.is_valid():
            servicio = form.save()
            return redirect('servicio_detail', pk=servicio.pk)
    else:
        form = ServicioForm(instance=servicio)
    return render(request, 'servicio/servicio_form.html', {'form': form})

@never_cache
@login_required
def eliminar_servicio(request, pk):
    servicio = get_object_or_404(Servicio, pk=pk)
    servicio.delete()
    return redirect(reverse('servicio_list'))


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
    search_column = request.GET.get('search_column', '')
    search_query = request.GET.get('search_query', '')
    filter_column = request.GET.get('filter_column', '')

    paquetes = Paquete.objects.all()

    # Aplicar búsqueda
    if search_column and search_query:
        if search_column in ['id', 'nombre_paquete', 'descripcion', 'precio']:
            paquetes = paquetes.filter(**{f"{search_column}__icontains": search_query})

    # Aplicar filtro
    if filter_column and filter_column != 'all':
        paquetes = paquetes.values('id', 'nombre_paquete', 'descripcion', 'precio', filter_column)
    else:
        paquetes = paquetes.values('id', 'nombre_paquete', 'descripcion', 'precio')

    paginator = Paginator(paquetes, 10)  # 10 paquetes por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'search_column': search_column,
        'search_query': search_query,
        'filter_column': filter_column,
    }

    return render(request, 'paquete/paquete_list.html', context)


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
    query = request.GET.get('query')
    column = request.GET.get('column')
    clientes = Cliente.objects.all()

    if query and column:
        if column == 'id':
            clientes = clientes.filter(id__icontains=query)
        elif column == 'nombre':
            clientes = clientes.filter(nombre__icontains=query)
        elif column == 'apellido':
            clientes = clientes.filter(apellido__icontains=query)
        elif column == 'email':
            clientes = clientes.filter(email__icontains=query)
        elif column == 'telefono':
            clientes = clientes.filter(telefono__icontains=query)
        elif column == 'direccion':
            clientes = clientes.filter(direccion__icontains=query)

    paginator = Paginator(clientes, 10)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)
    return render(request, 'cliente/cliente_list.html', {'page_obj': page_obj})

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
            return redirect('cliente_list')
    else:
        form = ClienteForm()
    return render(request, 'cliente/cliente_form.html', {'form': form})

@never_cache
@login_required
def cliente_edit(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == "POST":
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            cliente = form.save()
            return redirect('cliente_detail', pk=cliente.pk)
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'cliente/cliente_form.html', {'form': form})

@never_cache
@login_required
def eliminar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    cliente.delete()
    return redirect(reverse('cliente_list'))

# Reserva views
@never_cache
@login_required
def reserva_list(request):
    query = request.GET.get('query')
    column = request.GET.get('column')
    reservas = Reserva.objects.all()

    if query and column:
        if column == 'id':
            reservas = reservas.filter(id__icontains=query)
        elif column == 'fecha_reserva':
            reservas = reservas.filter(fecha_reserva__icontains=query)
        elif column == 'estado':
            reservas = reservas.filter(estado__icontains=query)
        elif column == 'cliente':
            reservas = reservas.filter(cliente__nombre__icontains=query) | reservas.filter(cliente__apellido__icontains=query)
        elif column == 'servicio':
            reservas = reservas.filter(servicio__tipo_de_servicio__icontains=query)

    paginator = Paginator(reservas, 10)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)
    return render(request, 'reserva/reserva_list.html', {'page_obj': page_obj})

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
            return redirect('reserva_list')
    else:
        form = ReservaForm()
    return render(request, 'reserva/reserva_form.html', {'form': form})

@never_cache
@login_required
def reserva_edit(request, pk):
    reserva = get_object_or_404(Reserva, pk=pk)
    if request.method == "POST":
        form = ReservaForm(request.POST, instance=reserva)
        if form.is_valid():
            reserva = form.save()
            return redirect('reserva_detail', pk=reserva.pk)
    else:
        form = ReservaForm(instance=reserva)
    return render(request, 'reserva/reserva_form.html', {'form': form})

@never_cache
@login_required
def eliminar_reserva(request, pk):
    reserva = get_object_or_404(Reserva, pk=pk)
    reserva.delete()
    return redirect(reverse('reserva_list'))

# Venta views
@never_cache
@login_required
def venta_list(request):
    query = request.GET.get('query')
    column = request.GET.get('column')
    ventas = Venta.objects.all()

    if query and column:
        if column == 'id':
            ventas = ventas.filter(id__icontains=query)
        elif column == 'fecha_venta':
            ventas = ventas.filter(fecha_venta__icontains=query)
        elif column == 'total':
            ventas = ventas.filter(total__icontains=query)
        elif column == 'cliente':
            ventas = ventas.filter(cliente__nombre__icontains=query) | ventas.filter(cliente__apellido__icontains=query)
        elif column == 'paquete':
            ventas = ventas.filter(paquete__nombre_paquete__icontains=query)

    paginator = Paginator(ventas, 10)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)
    return render(request, 'venta/venta_list.html', {'page_obj': page_obj})

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
            return redirect('venta_list')
    else:
        form = VentaForm()
    return render(request, 'venta/venta_form.html', {'form': form})

@never_cache
@login_required
def venta_edit(request, pk):
    venta = get_object_or_404(Venta, pk=pk)
    if request.method == "POST":
        form = VentaForm(request.POST, instance=venta)
        if form.is_valid():
            venta = form.save()
            return redirect('venta_detail', pk=venta.pk)
    else:
        form = VentaForm(instance=venta)
    return render(request, 'venta/venta_form.html', {'form': form})

@never_cache
@login_required
def eliminar_venta(request, pk):
    venta = get_object_or_404(Venta, pk=pk)
    venta.delete()
    return redirect(reverse('venta_list'))

# Foto views
@never_cache
@login_required
def foto_list(request):
    query = request.GET.get('query')
    column = request.GET.get('column')
    fotos = Foto.objects.all()

    if query and column:
        if column == 'id':
            fotos = fotos.filter(id__icontains=query)
        elif column == 'url':
            fotos = fotos.filter(url__icontains=query)
        elif column == 'descripcion':
            fotos = fotos.filter(descripcion__icontains=query)
        elif column == 'reserva':
            fotos = fotos.filter(reserva__id__icontains=query)

    paginator = Paginator(fotos, 10)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)
    return render(request, 'foto/foto_list.html', {'page_obj': page_obj})

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
            return redirect('foto_list')
    else:
        form = FotoForm()
    return render(request, 'foto/foto_form.html', {'form': form})

@never_cache
@login_required
def foto_edit(request, pk):
    foto = get_object_or_404(Foto, pk=pk)
    if request.method == "POST":
        form = FotoForm(request.POST, instance=foto)
        if form.is_valid():
            foto = form.save()
            return redirect('foto_detail', pk=foto.pk)
    else:
        form = FotoForm(instance=foto)
    return render(request, 'foto/foto_form.html', {'form': form})

@never_cache
@login_required
def eliminar_foto(request, pk):
    foto = get_object_or_404(Foto, pk=pk)
    foto.delete()
    return redirect(reverse('foto_list'))
