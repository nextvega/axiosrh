# Create your models here.
from django.db import models
from django.contrib.auth.hashers import make_password, is_password_usable

class Rol(models.Model):
    TIPO_CHOICES = [
        ('TEMPORAL', 'Temporal'),
        ('FIJO', 'Fijo'),
    ]

    ESTADO_CHOICES = [
        ('ACTIVO', 'Activo'),
        ('INACTIVO', 'Inactivo'),
    ]

    nombre = models.CharField(max_length=100)
    tipo_rol = models.CharField(max_length=10, choices=TIPO_CHOICES)
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES)
    comentarios = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Rol"
        verbose_name_plural = "Roles"

    def __str__(self):
        return self.nombre

class Permiso(models.Model):
    ESTADO_CHOICES = [
        ('ACTIVO', 'Activo'),
        ('INACTIVO', 'Inactivo'),
    ]

    nombre = models.CharField(max_length=100)
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES)
    comentarios = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Permiso"
        verbose_name_plural = "Permisos"

    def __str__(self):
        return self.nombre

class AsignarPermiso(models.Model):
    rol = models.OneToOneField(Rol, on_delete=models.CASCADE, related_name='permisos_asignados')
    permisos = models.ManyToManyField(Permiso, related_name='roles_asignados')

    class Meta:
        verbose_name = "Asignación de Permisos"
        verbose_name_plural = "Asignaciones de Permisos"

    def __str__(self):
        return f"Permisos de {self.rol.nombre}"
    
class Usuario(models.Model):
    ESTADO_CHOICES = [
        ('ACTIVO', 'Activo'),
        ('INACTIVO', 'Inactivo'),
    ]

    nombre = models.CharField(max_length=100)
    usuario = models.CharField(max_length=50, unique=True)
    contraseña = models.CharField(max_length=128)  # Usualmente se guarda el hash de la contraseña
    telefono = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(unique=True)
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='ACTIVO')
    rol = models.ForeignKey('Rol', on_delete=models.PROTECT, related_name='usuarios')

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

    def __str__(self):
        return self.nombre
    
    def save(self, *args, **kwargs):
        if self.contraseña and not is_password_usable(self.contraseña):
            self.contraseña = make_password(self.contraseña)
        super().save(*args, **kwargs)

class Cargo(models.Model):
    ESTADOS = [
        ('ACTIVO', 'Activo'),
        ('INACTIVO', 'Inactivo'),
    ]

    nombre = models.CharField(max_length=100, unique=True)
    estado = models.CharField(max_length=10, choices=ESTADOS)
    comentarios = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Cargo"
        verbose_name_plural = "Cargos"

    def __str__(self):
        return self.nombre
    
class Empleado(models.Model):
    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    ]

    ESTADO_CHOICES = [
        ('ACTIVO', 'Activo'),
        ('INACTIVO', 'Inactivo'),
    ]

    TIPO_PAGO_CHOICES = [
        ('QUINCENAL', 'Quincenal'),
        ('MENSUAL', 'Mensual'),
        ('SEMANAL', 'Semanal'),
    ]

    SI_NO_CHOICES = [
        ('SI', 'Sí'),
        ('NO', 'No'),
    ]

    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    domicilio = models.TextField()
    telefono = models.CharField(max_length=15)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    nacionalidad = models.CharField(max_length=50, null=True)
    departamento = models.CharField(max_length=100, null=True)
    municipio = models.CharField(max_length=100, null=True)
    # distrito = models.CharField(max_length=100, null=True)
    dui = models.CharField(max_length=10, blank=True)
    nit = models.CharField(max_length=17, blank=True)
    seguro = models.CharField(max_length=20, blank=True, null=True)
    afp = models.CharField(max_length=20, blank=True, null=True)
    fecha_ingreso = models.DateField()
    fecha_salida = models.DateField(blank=True, null=True)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    tipo_cargo = models.ForeignKey(Cargo, on_delete=models.PROTECT)
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES)
    tipo_pago = models.CharField(max_length=10, choices=TIPO_PAGO_CHOICES)
    eventual = models.CharField(max_length=2, choices=SI_NO_CHOICES)
    comentarios = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"

    def __str__(self):
        return self.nombre