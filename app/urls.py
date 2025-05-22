from django.urls import path

from . import views

urlpatterns = [
    # Login
    path("login/", views.login, name="login"),

    # General
    path("", views.index, name="index"),
    # roles
    path("administracion/roles/", views.roles, name="roles"),
    path("administracion/roles/nuevo_rol", views.nuevo_rol, name="nuevo_rol"),
    path('administracion/roles/editar_rol/<int:pk>/', views.editar_rol, name='editar_rol'),
    path('administracion/roles/eliminar_rol/<int:pk>/', views.eliminar_rol, name='eliminar_rol'),

    # permisos
    path("administracion/permisos_admin/", views.permisos_admin, name="permisos_admin"),
    path("administracion/permisos_admin/nuevo_permiso", views.nuevo_permiso, name="nuevo_permiso"),
    path("administracion/permisos_admin/editar_permiso/<int:pk>/", views.editar_permiso, name="editar_permiso"),
    path("administracion/permisos_admin/eliminar_permiso/<int:pk>/", views.eliminar_permiso, name="eliminar_permiso"),

    # asignar permisos
    path("administracion/asignar_permisos/", views.asignar_permisos, name="asignar_permisos"),
    path("administracion/asignar_permisos/nuevo_asignar_permiso", views.nuevo_asignar_permiso, name="nuevo_asignar_permiso"),      
    path("administracion/asignar_permisos/editar_asignar_permiso/<int:pk>/", views.editar_asignar_permiso, name="editar_asignar_permiso"),  
    path("administracion/asignar_permisos/eliminar_asignar_permiso/<int:pk>/", views.eliminar_asignar_permiso, name="eliminar_asignar_permiso"),  

    # usuarios
    path("administracion/usuarios/", views.usuarios, name="usuarios"),
    path("administracion/usuarios/nuevo_usuario", views.nuevo_usuario, name="nuevo_usuario"),
    path("administracion/usuarios/editar_usuario/<int:pk>/", views.editar_usuario, name="editar_usuario"),
    path("administracion/usuarios/eliminar_usuario/<int:pk>/", views.eliminar_usuario, name="eliminar_usuario"),

    # Modulos -> Permisos
    path("permisos/tipo_permisos", views.tipo_permisos, name="tipo_permisos"),
    path("permisos/permisos", views.permisos, name="permisos"),

    # Modulos -> Reclutamiento
    path("reclutamiento/vacantes_disponibles", views.vacantes_disponibles, name="vacantes_disponibles"),
    path("reclutamiento/candidatos", views.candidatos, name="candidatos"),
    path("reclutamiento/referidos", views.referidos, name="referidos"),

    # Modulos -> Empleados

    # cargos
    path("empleados/cargos", views.cargos, name="cargos"),
    path("empleados/cargos/nuevo_cargo", views.nuevo_cargo, name="nuevo_cargo"),
    path("empleados/cargos/editar_cargo/<int:pk>/", views.editar_cargo, name="editar_cargo"),
    path("empleados/cargos/eliminar_cargo/<int:pk>/", views.eliminar_cargo, name="eliminar_cargo"),


    # empleados
    path("empleados/empleados", views.empleados, name="empleados"),
    path("empleados/empleados/nuevo_empleado/", views.nuevo_empleado, name="nuevo_empleado"),
    path("empleados/empleados/editar_empleado/<int:pk>/", views.editar_empleado, name="editar_empleado"),
    path("empleados/empleados/eliminar_empleado/<int:pk>/", views.eliminar_empleado, name="eliminar_empleado"),



    # Modulos -> Historicos
    path("historicos/historico_empleados", views.historico_empleados, name="historico_empleados"),
    path("historicos/historico_candidatos", views.historico_candidatos, name="historico_candidatos"),

    # Modulos -> Planillas
    path("planillas/planilla_mensuales", views.planilla_mensuales, name="planilla_mensuales"),
    path("planillas/planilla_quincenales", views.planilla_quincenales, name="planilla_quincenales"),
    path("planillas/planilla_semanales", views.planilla_semanales, name="planilla_semanales"),
    path("planillas/planilla_eventuales", views.planilla_eventuales, name="planilla_eventuales"),

    # Modulos -> Retenciones
    path("retenciones/retenciones_ley", views.retenciones_ley, name="retenciones_ley"),
    path("retenciones/retenciones_renta", views.retenciones_renta, name="retenciones_renta"),

    # Modulos -> Empleados Permisos
    path("empleados_permisos/permisos_medicos", views.permisos_medicos, name="permisos_medicos"),
    path("empleados_permisos/permisos_personales", views.permisos_personales, name="permisos_personales"),
    path("empleados_permisos/vacaciones", views.vacaciones, name="vacaciones"),

    # Modulos -> Empresa
    path("empresa/empresa", views.empresa, name="empresa"),

    # Sistema
    path("ajustes_generales/ajustes_generales", views.ajustes_generales, name="ajustes_generales"),
]