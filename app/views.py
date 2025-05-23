from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone
from django.http import JsonResponse
from django.urls import reverse
from django.conf import settings
from django.contrib import messages
from .models import Rol, Permiso, AsignarPermiso, Usuario, Cargo, Empleado, Permisos
from django.core.paginator import Paginator
from .forms import RolForm, PermisoForm, AsignarPermisoForm, UsuarioForm, CargoForm, EmpleadoForm, TipoPermiso, TipoPermisoForm, PermisosForm
from django.db.models import Q
# Login

def login(request):
    return render(request, 'pages/login/login.html',{
        'title': 'Welcome'
    })

# Dashboard.

def index(request):
    return render(request, 'pages/dashboard/dashboard.html',{
        'title': 'Dashboard'
    })


# General -> Administracion
# roles
def roles(request):
    query = request.GET.get('buscador', '').strip()
    roles_list = Rol.objects.all()

    if query:
        roles_list = roles_list.filter(nombre__icontains=query)

    roles_list = roles_list.order_by('-id')  

    paginator = Paginator(roles_list, 10)
    page_number = request.GET.get('page')
    roles = paginator.get_page(page_number)

    return render(request, 'pages/administracion/roles.html',{
        'title': 'Roles',
        'roles': roles,
        'query': query,
    })

def nuevo_rol(request):
    if request.method == 'POST':
        form = RolForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Rol creado correctamente.', extra_tags='create')
            return redirect('roles')
        else:
            messages.error(request, 'Por favor corrige los errores del formulario.', extra_tags='error')
    else:
        form = RolForm()

    return render(request, 'pages/administracion/forms/form_rol.html',{
        'title': 'Nuevo Rol',
        'form': form,
    })

def editar_rol(request, pk):
    rol = get_object_or_404(Rol, pk=pk)

    if request.method == 'POST':
        form = RolForm(request.POST, instance=rol)
        if form.is_valid():
            form.save()
            messages.success(request, 'Rol actualizado exitosamente.', extra_tags='update')
            return redirect('roles')  # Cambia a la vista de lista de roles
    else:
        form = RolForm(instance=rol)

    return render(request, 'pages/administracion/forms/form_rol.html', {
        'form': form,
        'title': 'Editar Rol'
    })

def eliminar_rol(request, pk):
    rol = get_object_or_404(Rol, pk=pk)
    rol.delete()
    messages.success(request, 'Rol eliminado exitosamente.', extra_tags='delete')
    return redirect('roles')



# permisos
def permisos_admin(request):
    query = request.GET.get('buscador', '').strip()
    permisos_list = Permiso.objects.all()

    if query:
        permisos_list = permisos_list.filter(nombre__icontains=query)

    permisos_list = permisos_list.order_by('-id')

    paginator = Paginator(permisos_list, 10)
    page_number = request.GET.get('page')
    permisos = paginator.get_page(page_number)

    return render(request, 'pages/administracion/permisos.html', {
        'title': 'Permisos',
        'permisos': permisos,
        'query': query,
    })

def nuevo_permiso(request):
    if request.method == 'POST':
        form = PermisoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Permiso creado correctamente.', extra_tags='create')
            return redirect('permisos_admin')  # Cambia 'permisos' al nombre de tu vista de lista de permisos
        else:
            messages.error(request, 'Por favor corrige los errores del formulario.', extra_tags='error')
    else:
        form = PermisoForm()

    return render(request, 'pages/administracion/forms/form_permiso.html', {
        'title': 'Nuevo Permiso',
        'form': form,
    })

def editar_permiso(request, pk):
    permiso = get_object_or_404(Permiso, pk=pk)

    if request.method == 'POST':
        form = PermisoForm(request.POST, instance=permiso)
        if form.is_valid():
            form.save()
            messages.success(request, 'Permiso actualizado exitosamente.', extra_tags='update')
            return redirect('permisos_admin')  # Cambia a la vista de lista de permisos
    else:
        form = PermisoForm(instance=permiso)

    return render(request, 'pages/administracion/forms/form_permiso.html', {
        'form': form,
        'title': 'Editar Permiso'
    })

def eliminar_permiso(request, pk):
    permiso = get_object_or_404(Permiso, pk=pk)
    permiso.delete()
    messages.success(request, 'Permiso eliminado exitosamente.', extra_tags='delete')
    return redirect('permisos_admin')  # Cambia 'permisos' por el nombre de tu vista de lista de permisos


# asignar permisos
def asignar_permisos(request):
    query = request.GET.get('buscador', '').strip()
    asignar_permisos_list = AsignarPermiso.objects.all()

    if query:
        asignar_permisos_list = asignar_permisos_list.filter(rol__nombre__icontains=query)

    asignar_permisos_list = asignar_permisos_list.order_by('-id')

    paginator = Paginator(asignar_permisos_list, 10)
    page_number = request.GET.get('page')
    asignar_permisos = paginator.get_page(page_number)

    return render(request, 'pages/administracion/asignar_permisos.html', {
        'title': 'Asignar Permisos',
        'asignar_permisos': asignar_permisos,
        'query': query,
    })

def nuevo_asignar_permiso(request):
    if request.method == 'POST':
        form = AsignarPermisoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Permisos asignados correctamente.', extra_tags='create')
            return redirect('asignar_permisos')  # Cambia al nombre correcto de tu vista de lista de asignaciones
        else:
            messages.error(request, 'Por favor corrige los errores del formulario.', extra_tags='error')
    else:
        form = AsignarPermisoForm()

    return render(request, 'pages/administracion/forms/form_asignar_permiso.html', {
        'title': 'Asignar Permisos',
        'form': form,
    })

def editar_asignar_permiso(request, pk):
    asignacion = get_object_or_404(AsignarPermiso, pk=pk)

    if request.method == 'POST':
        form = AsignarPermisoForm(request.POST, instance=asignacion)
        if form.is_valid():
            form.save()
            messages.success(request, 'Permisos asignados actualizados correctamente.', extra_tags='update')
            return redirect('asignar_permisos')  # Cambia al nombre correcto de tu vista de listado
        else:
            messages.error(request, 'Por favor corrige los errores del formulario.', extra_tags='error')
    else:
        form = AsignarPermisoForm(instance=asignacion)

    return render(request, 'pages/administracion/forms/form_asignar_permiso.html', {
        'form': form,
        'title': 'Editar Asignación de Permisos',
    })

def eliminar_asignar_permiso(request, pk):
    asignacion = get_object_or_404(AsignarPermiso, pk=pk)
    asignacion.delete()
    messages.success(request, 'Asignación de permisos eliminada exitosamente.', extra_tags='delete')
    return redirect('asignar_permisos')


# usuarios
def usuarios(request):
    query = request.GET.get('buscador', '').strip()
    usuarios_list = Usuario.objects.all()

    if query:
        usuarios_list = usuarios_list.filter(
            Q(nombre__icontains=query) | Q(usuario__icontains=query)
        )

    usuarios_list = usuarios_list.order_by('-id')

    paginator = Paginator(usuarios_list, 10)
    page_number = request.GET.get('page')
    usuarios = paginator.get_page(page_number)

    return render(request, 'pages/administracion/usuarios.html', {
        'title': 'Usuarios',
        'usuarios': usuarios,
        'query': query,
    })

def nuevo_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario creado correctamente.', extra_tags='create')
            return redirect('usuarios') 
        else:
            messages.error(request, 'Por favor corrige los errores del formulario.', extra_tags='error')
    else:
        form = UsuarioForm()

    return render(request, 'pages/administracion/forms/form_usuario.html', {
        'title': 'Nuevo Usuario',
        'form': form,
    })

def editar_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)

    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario actualizado exitosamente.', extra_tags='update')
            return redirect('usuarios')  # Ajusta el nombre de la vista de listado de usuarios si es diferente
    else:
        form = UsuarioForm(instance=usuario)

    return render(request, 'pages/administracion/forms/form_usuario.html', {
        'form': form,
        'title': 'Editar Usuario',
    })

def eliminar_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    usuario.delete()
    messages.success(request, 'Usuario eliminado correctamente.', extra_tags='delete')
    return redirect('usuarios') 


# Modulos -> Empleados

# cargos
def cargos(request):
    query = request.GET.get('buscador', '').strip()
    cargos_list = Cargo.objects.all()

    if query:
        cargos_list = cargos_list.filter(nombre__icontains=query)

    cargos_list = cargos_list.order_by('-id')

    paginator = Paginator(cargos_list, 10)
    page_number = request.GET.get('page')
    cargos = paginator.get_page(page_number)

    return render(request, 'pages/empleados/cargos.html', {
        'title': 'Cargos',
        'cargos': cargos,
        'query': query,
    })

def nuevo_cargo(request):
    if request.method == 'POST':
        form = CargoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cargo creado exitosamente.', extra_tags='create')
            return redirect('cargos')
    else:
        form = CargoForm()

    return render(request, 'pages/empleados/forms/form_cargo.html', {
        'form': form,
        'title': 'Nuevo Cargo',
    })

def editar_cargo(request, pk):
    cargo = get_object_or_404(Cargo, pk=pk)

    if request.method == 'POST':
        form = CargoForm(request.POST, instance=cargo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cargo actualizado exitosamente.', extra_tags='update')
            return redirect('cargos')
    else:
        form = CargoForm(instance=cargo)

    return render(request, 'pages/empleados/forms/form_cargo.html', {
        'form': form,
        'title': 'Editar Cargo',
    })

def eliminar_cargo(request, pk):
    cargo = get_object_or_404(Cargo, pk=pk)
    cargo.delete()
    messages.success(request, 'Cargo eliminado exitosamente.', extra_tags='delete')
    return redirect('cargos')


# empleados
def empleados(request):
    query = request.GET.get('buscador', '').strip()
    empleados_list = Empleado.objects.all()

    if query:
        empleados_list = empleados_list.filter(nombre__icontains=query)

    empleados_list = empleados_list.order_by('-id')

    paginator = Paginator(empleados_list, 10)
    page_number = request.GET.get('page')
    empleados = paginator.get_page(page_number)

    return render(request, 'pages/empleados/empleados.html', {
        'title': 'Empleados',
        'empleados': empleados,
        'query': query,
    })

def nuevo_empleado(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Empleado creado exitosamente.', extra_tags='create')
            return redirect('empleados')  # Asegúrate que esta URL exista en tu proyecto
    else:
        form = EmpleadoForm()

    return render(request, 'pages/empleados/forms/form_empleado.html', {
        'form': form,
        'title': 'Nuevo Empleado',
    })

def editar_empleado(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk)

    if request.method == 'POST':
        form = EmpleadoForm(request.POST, instance=empleado)
        if form.is_valid():
            form.save()
            messages.success(request, 'Empleado actualizado exitosamente.', extra_tags='update')
            return redirect('empleados')  # Asegúrate de que 'empleados' sea el nombre correcto en tus URLs
    else:
        form = EmpleadoForm(instance=empleado)

    return render(request, 'pages/empleados/forms/form_empleado.html', {
        'form': form,
        'title': 'Editar Empleado',
    })

def eliminar_empleado(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    empleado.delete()
    messages.success(request, 'Empleado eliminado exitosamente.', extra_tags='delete')
    return redirect('empleados')

# Modulos -> Permisos 

# tipo de permisos
def empleado_tipo_permisos(request):
    query = request.GET.get('buscador', '').strip()
    tipo_permisos_list = TipoPermiso.objects.all()

    if query:
        tipo_permisos_list = tipo_permisos_list.filter(nombre__icontains=query)

    tipo_permisos_list = tipo_permisos_list.order_by('-id')

    paginator = Paginator(tipo_permisos_list, 10)
    page_number = request.GET.get('page')
    tipo_permisos = paginator.get_page(page_number)

    return render(request, 'pages/permisos/tipo_permisos.html', {
        'title': 'Tipos de Permisos',
        'tipo_permisos': tipo_permisos,
        'query': query,
    })

def empleado_nuevo_tipo_permiso(request):
    if request.method == 'POST':
        form = TipoPermisoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tipo de permiso creado exitosamente.', extra_tags='create')
            return redirect('empleado_tipo_permisos')
    else:
        form = TipoPermisoForm()

    return render(request, 'pages/permisos/forms/form_tipo_permiso.html', {
        'form': form,
        'title': 'Nuevo Tipo de Permiso',
    })

def empleado_editar_tipo_permiso(request, pk):
    tipo_permiso = get_object_or_404(TipoPermiso, pk=pk)

    if request.method == 'POST':
        form = TipoPermisoForm(request.POST, instance=tipo_permiso)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tipo de permiso actualizado exitosamente.', extra_tags='update')
            return redirect('empleado_tipo_permisos')
    else:
        form = TipoPermisoForm(instance=tipo_permiso)

    return render(request, 'pages/permisos/forms/form_tipo_permiso.html', {
        'form': form,
        'title': 'Editar Tipo de Permiso',
    })

def empleado_eliminar_tipo_permiso(request, pk):
    tipo_permiso = get_object_or_404(TipoPermiso, pk=pk)
    tipo_permiso.delete()
    messages.success(request, 'Tipo de permiso eliminado exitosamente.', extra_tags='delete')
    return redirect('empleado_tipo_permisos')

# permisos
def permisos(request):
    query = request.GET.get('buscador', '').strip()
    permisos_list = Permisos.objects.select_related('empleado', 'tipo_permiso').all()

    if query:
        # Filtramos por nombre del empleado o nombre del tipo permiso (puedes ajustar según necesites)
        permisos_list = permisos_list.filter(
            empleado__nombre__icontains=query
        ) | permisos_list.filter(
            tipo_permiso__nombre__icontains=query
        )

    permisos_list = permisos_list.order_by('-id')

    paginator = Paginator(permisos_list, 10)
    page_number = request.GET.get('page')
    permisos = paginator.get_page(page_number)

    return render(request, 'pages/permisos/permisos.html', {
        'title': 'Permisos',
        'permisos': permisos,
        'query': query,
    })

def nuevo_permisos(request):
    if request.method == 'POST':
        form = PermisosForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Permiso creado exitosamente.', extra_tags='create')
            return redirect('permisos')  # Cambia 'permisos' por el nombre correcto de la url que lista permisos
    else:
        form = PermisosForm()

    return render(request, 'pages/permisos/forms/form_permiso.html', {
        'form': form,
        'title': 'Nuevo Permiso',
    })

def editar_permisos(request, pk):
    permiso = get_object_or_404(Permisos, pk=pk)

    if request.method == 'POST':
        form = PermisosForm(request.POST, instance=permiso)
        if form.is_valid():
            form.save()
            messages.success(request, 'Permiso actualizado exitosamente.', extra_tags='update')
            return redirect('permisos')  # Cambia por la url donde listan los permisos
    else:
        form = PermisosForm(instance=permiso)

    return render(request, 'pages/permisos/forms/form_permiso.html', {
        'form': form,
        'title': 'Editar Permiso',
    })

def eliminar_permisos(request, pk):
    permiso = get_object_or_404(Permisos, pk=pk)
    permiso.delete()
    messages.success(request, 'Permiso eliminado exitosamente.', extra_tags='delete')
    return redirect('permisos') 

# Modulos -> Reclutamiento 

def vacantes_disponibles(request):
    return render(request, 'pages/reclutamiento/vacantes_disponibles.html',{
        'title': 'Vacantes Disponibles',
    })

def candidatos(request):
    return render(request, 'pages/reclutamiento/candidatos.html',{
        'title': 'Candidatos',
    })

def referidos(request):
    return render(request, 'pages/reclutamiento/referidos.html',{
        'title': 'Referidos',
    })



# Modulos -> Historicos

def historico_empleados(request):
    return render(request, 'pages/historicos/historico_empleados.html',{
        'title': 'Historico Empleados',
    })

def historico_candidatos(request):
    return render(request, 'pages/historicos/historico_candidatos.html',{
        'title': 'Historico Candidatos',
    })


# Modulos -> Planillas

def planilla_mensuales(request):
    return render(request, 'pages/planillas/mensuales.html',{
        'title': 'Planilla Mensual',
    })

def planilla_quincenales(request):
    return render(request, 'pages/planillas/quincenales.html',{
        'title': 'Planilla Quincenal',
    })

def planilla_semanales(request):
    return render(request, 'pages/planillas/semanales.html',{
        'title': 'Planilla Semanal',
    })

def planilla_eventuales(request):
    return render(request, 'pages/planillas/eventuales.html',{
        'title': 'Planilla Eventual',
    })


# Modulos -> Retenciones

def retenciones_ley(request):
    return render(request, 'pages/retenciones/retenciones_ley.html',{
        'title': 'Retenciones De Ley',
    })

def retenciones_renta(request):
    return render(request, 'pages/retenciones/retenciones_renta.html',{
        'title': 'Retenciones De Renta',
    })


# Modulos -> Emple. Permisos

def permisos_medicos(request):
    return render(request, 'pages/empleados_permisos/permisos_medicos.html',{
        'title': 'Permisos Medicos',
    })

def permisos_personales(request):
    return render(request, 'pages/empleados_permisos/permisos_personales.html',{
        'title': 'Permisos Personales',
    })

def vacaciones(request):
    return render(request, 'pages/empleados_permisos/vacaciones.html',{
        'title': 'Vacaciones',
    })


# Modulos -> Empresa

def empresa(request):
    return render(request, 'pages/empresa/empresa.html',{
        'title': 'Empresa',
    })

# Sistema

def ajustes_generales(request):
    return render(request, 'pages/ajustes_generales/ajustes_generales.html',{
        'title': 'Empresa',
    })
