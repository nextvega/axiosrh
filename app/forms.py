from django import forms
from .models import Rol, Permiso, AsignarPermiso, Usuario, Cargo, Empleado, TipoPermiso, Permisos
from django.contrib.auth.hashers import make_password
from django.forms import DateInput

# funciones y clases para consumir
def obtener_paises():
    return [
        ('', '---------'),        
        ('OT', 'Otro'),
        ('AF', 'Afganistán'),
        ('AL', 'Albania'),
        ('DZ', 'Argelia'),
        ('AS', 'Samoa Americana'),
        ('AD', 'Andorra'),
        ('AO', 'Angola'),
        ('AI', 'Anguilla'),
        ('AQ', 'Antártida'),
        ('AG', 'Antigua y Barbuda'),
        ('AR', 'Argentina'),
        ('AM', 'Armenia'),
        ('AW', 'Aruba'),
        ('AU', 'Australia'),
        ('AT', 'Austria'),
        ('AZ', 'Azerbaiyán'),
        ('BS', 'Bahamas'),
        ('BH', 'Baréin'),
        ('BD', 'Bangladés'),
        ('BB', 'Barbados'),
        ('BY', 'Bielorrusia'),
        ('BE', 'Bélgica'),
        ('BZ', 'Belice'),
        ('BJ', 'Benín'),
        ('BM', 'Bermudas'),
        ('BT', 'Bután'),
        ('BO', 'Bolivia'),
        ('BA', 'Bosnia y Herzegovina'),
        ('BW', 'Botsuana'),
        ('BR', 'Brasil'),
        ('BN', 'Brunéi'),
        ('BG', 'Bulgaria'),
        ('BF', 'Burkina Faso'),
        ('BI', 'Burundi'),
        ('KH', 'Camboya'),
        ('CM', 'Camerún'),
        ('CA', 'Canadá'),
        ('CV', 'Cabo Verde'),
        ('KY', 'Islas Caimán'),
        ('CF', 'República Centroafricana'),
        ('TD', 'Chad'),
        ('CL', 'Chile'),
        ('CN', 'China'),
        ('CX', 'Isla de Navidad'),
        ('CO', 'Colombia'),
        ('KM', 'Comoras'),
        ('CG', 'República del Congo'),
        ('CD', 'República Democrática del Congo'),
        ('CK', 'Islas Cook'),
        ('CR', 'Costa Rica'),
        ('CI', 'Costa de Marfil'),
        ('HR', 'Croacia'),
        ('CU', 'Cuba'),
        ('CY', 'Chipre'),
        ('CZ', 'República Checa'),
        ('DK', 'Dinamarca'),
        ('DJ', 'Yibuti'),
        ('DM', 'Dominica'),
        ('DO', 'República Dominicana'),
        ('EC', 'Ecuador'),
        ('EG', 'Egipto'),
        ('SV', 'El Salvador'),
        ('GQ', 'Guinea Ecuatorial'),
        ('ER', 'Eritrea'),
        ('EE', 'Estonia'),
        ('SZ', 'Esuatini'),
        ('ET', 'Etiopía'),
        ('FJ', 'Fiyi'),
        ('FI', 'Finlandia'),
        ('FR', 'Francia'),
        ('GA', 'Gabón'),
        ('GM', 'Gambia'),
        ('GE', 'Georgia'),
        ('DE', 'Alemania'),
        ('GH', 'Ghana'),
        ('GR', 'Grecia'),
        ('GD', 'Granada'),
        ('GU', 'Guam'),
        ('GT', 'Guatemala'),
        ('GN', 'Guinea'),
        ('GW', 'Guinea-Bisáu'),
        ('GY', 'Guyana'),
        ('HT', 'Haití'),
        ('HN', 'Honduras'),
        ('HK', 'Hong Kong'),
        ('HU', 'Hungría'),
        ('IS', 'Islandia'),
        ('IN', 'India'),
        ('ID', 'Indonesia'),
        ('IR', 'Irán'),
        ('IQ', 'Irak'),
        ('IE', 'Irlanda'),
        ('IL', 'Israel'),
        ('IT', 'Italia'),
        ('JM', 'Jamaica'),
        ('JP', 'Japón'),
        ('JO', 'Jordania'),
        ('KZ', 'Kazajistán'),
        ('KE', 'Kenia'),
        ('KI', 'Kiribati'),
        ('KP', 'Corea del Norte'),
        ('KR', 'Corea del Sur'),
        ('KW', 'Kuwait'),
        ('KG', 'Kirguistán'),
        ('LA', 'Laos'),
        ('LV', 'Letonia'),
        ('LB', 'Líbano'),
        ('LS', 'Lesoto'),
        ('LR', 'Liberia'),
        ('LY', 'Libia'),
        ('LI', 'Liechtenstein'),
        ('LT', 'Lituania'),
        ('LU', 'Luxemburgo'),
        ('MO', 'Macao'),
        ('MG', 'Madagascar'),
        ('MW', 'Malawi'),
        ('MY', 'Malasia'),
        ('MV', 'Maldivas'),
        ('ML', 'Malí'),
        ('MT', 'Malta'),
        ('MH', 'Islas Marshall'),
        ('MR', 'Mauritania'),
        ('MU', 'Mauricio'),
        ('MX', 'México'),
        ('FM', 'Micronesia'),
        ('MD', 'Moldavia'),
        ('MC', 'Mónaco'),
        ('MN', 'Mongolia'),
        ('ME', 'Montenegro'),
        ('MA', 'Marruecos'),
        ('MZ', 'Mozambique'),
        ('MM', 'Birmania'),
        ('NA', 'Namibia'),
        ('NR', 'Nauru'),
        ('NP', 'Nepal'),
        ('NL', 'Países Bajos'),
        ('NZ', 'Nueva Zelanda'),
        ('NI', 'Nicaragua'),
        ('NE', 'Níger'),
        ('NG', 'Nigeria'),
        ('NO', 'Noruega'),
        ('OM', 'Omán'),
        ('PK', 'Pakistán'),
        ('PW', 'Palaos'),
        ('PA', 'Panamá'),
        ('PG', 'Papúa Nueva Guinea'),
        ('PY', 'Paraguay'),
        ('PE', 'Perú'),
        ('PH', 'Filipinas'),
        ('PL', 'Polonia'),
        ('PT', 'Portugal'),
        ('PR', 'Puerto Rico'),
        ('QA', 'Qatar'),
        ('RO', 'Rumania'),
        ('RU', 'Rusia'),
        ('RW', 'Ruanda'),
        ('KN', 'San Cristóbal y Nieves'),
        ('LC', 'Santa Lucía'),
        ('VC', 'San Vicente y las Granadinas'),
        ('WS', 'Samoa'),
        ('SM', 'San Marino'),
        ('ST', 'Santo Tomé y Príncipe'),
        ('SA', 'Arabia Saudita'),
        ('SN', 'Senegal'),
        ('RS', 'Serbia'),
        ('SC', 'Seychelles'),
        ('SL', 'Sierra Leona'),
        ('SG', 'Singapur'),
        ('SK', 'Eslovaquia'),
        ('SI', 'Eslovenia'),
        ('SB', 'Islas Salomón'),
        ('SO', 'Somalia'),
        ('ZA', 'Sudáfrica'),
        ('SS', 'Sudán del Sur'),
        ('ES', 'España'),
        ('LK', 'Sri Lanka'),
        ('SD', 'Sudán'),
        ('SR', 'Surinam'),
        ('SE', 'Suecia'),
        ('CH', 'Suiza'),
        ('SY', 'Siria'),
        ('TW', 'Taiwán'),
        ('TJ', 'Tayikistán'),
        ('TZ', 'Tanzania'),
        ('TH', 'Tailandia'),
        ('TL', 'Timor-Leste'),
        ('TG', 'Togo'),
        ('TO', 'Tonga'),
        ('TT', 'Trinidad y Tobago'),
        ('TN', 'Túnez'),
        ('TR', 'Turquía'),
        ('TM', 'Turkmenistán'),
        ('TV', 'Tuvalu'),
        ('UG', 'Uganda'),
        ('UA', 'Ucrania'),
        ('AE', 'Emiratos Árabes Unidos'),
        ('GB', 'Reino Unido'),
        ('US', 'Estados Unidos'),
        ('UY', 'Uruguay'),
        ('UZ', 'Uzbekistán'),
        ('VU', 'Vanuatu'),
        ('VE', 'Venezuela'),
        ('VN', 'Vietnam'),
        ('YE', 'Yemen'),
        ('ZM', 'Zambia'),
        ('ZW', 'Zimbabue'),
    ]

def obtener_departamentos():
    return [
        ('', '---------'),     
        ('OT', 'Otro'),
        ('AH', 'Ahuachapán'),
        ('CA', 'Cabañas'),
        ('CH', 'Chalatenango'),
        ('CU', 'Cuscatlán'),
        ('LI', 'La Libertad'),
        ('PA', 'La Paz'),
        ('UN', 'La Unión'),
        ('MO', 'Morazán'),
        ('SM', 'San Miguel'),
        ('SS', 'San Salvador'),
        ('SV', 'San Vicente'),
        ('SA', 'Santa Ana'),
        ('SO', 'Sonsonate'),
        ('US', 'Usulután'),
    ]

def obtener_municipios():
    return [
        # Ahuachapán
        ('', '---------'),     
        ('OT', 'Otro'),
        ('Ahuachapán', 'Ahuachapán'),
        ('Atiquizaya', 'Atiquizaya'),
        ('Apaneca', 'Apaneca'),
        ('Tacuba', 'Tacuba'),
        ('Turín', 'Turín'),

        # Cabañas
        ('Sensuntepeque', 'Sensuntepeque'),
        ('Ilobasco', 'Ilobasco'),
        ('Victoria', 'Victoria'),
        ('Dolores', 'Dolores'),
        ('Tejutepeque', 'Tejutepeque'),

        # Chalatenango
        ('Chalatenango', 'Chalatenango'),
        ('La Palma', 'La Palma'),
        ('Nueva Concepción', 'Nueva Concepción'),
        ('Agua Caliente', 'Agua Caliente'),
        ('Tejutla', 'Tejutla'),

        # Cuscatlán
        ('Cojutepeque', 'Cojutepeque'),
        ('Suchitoto', 'Suchitoto'),
        ('San Pedro Perulapán', 'San Pedro Perulapán'),
        ('San Rafael Cedros', 'San Rafael Cedros'),
        ('Candelaria', 'Candelaria'),

        # La Libertad
        ('Santa Tecla', 'Santa Tecla'),
        ('Antiguo Cuscatlán', 'Antiguo Cuscatlán'),
        ('Zaragoza', 'Zaragoza'),
        ('Colón', 'Colón'),
        ('La Libertad', 'La Libertad'),

        # La Paz
        ('Zacatecoluca', 'Zacatecoluca'),
        ('Olocuilta', 'Olocuilta'),
        ('San Pedro Masahuat', 'San Pedro Masahuat'),
        ('El Rosario', 'El Rosario'),
        ('San Luis Talpa', 'San Luis Talpa'),

        # La Unión
        ('La Unión', 'La Unión'),
        ('Santa Rosa de Lima', 'Santa Rosa de Lima'),
        ('Anamorós', 'Anamorós'),
        ('Conchagua', 'Conchagua'),
        ('El Sauce', 'El Sauce'),

        # Morazán
        ('San Francisco Gotera', 'San Francisco Gotera'),
        ('Perquín', 'Perquín'),
        ('Joateca', 'Joateca'),
        ('Cacaopera', 'Cacaopera'),
        ('Delicias de Concepción', 'Delicias de Concepción'),

        # San Miguel
        ('San Miguel', 'San Miguel'),
        ('Ciudad Barrios', 'Ciudad Barrios'),
        ('Chinameca', 'Chinameca'),
        ('Moncagua', 'Moncagua'),
        ('Nueva Guadalupe', 'Nueva Guadalupe'),

        # San Salvador
        ('San Salvador', 'San Salvador'),
        ('Soyapango', 'Soyapango'),
        ('Mejicanos', 'Mejicanos'),
        ('Apopa', 'Apopa'),
        ('Ilopango', 'Ilopango'),

        # San Vicente
        ('San Vicente', 'San Vicente'),
        ('Tecoluca', 'Tecoluca'),
        ('Verapaz', 'Verapaz'),
        ('Guadalupe', 'Guadalupe'),
        ('Apastepeque', 'Apastepeque'),

        # Santa Ana
        ('Santa Ana', 'Santa Ana'),
        ('Metapán', 'Metapán'),
        ('Chalchuapa', 'Chalchuapa'),
        ('Candelaria de la Frontera', 'Candelaria de la Frontera'),
        ('Coatepeque', 'Coatepeque'),

        # Sonsonate
        ('Sonsonate', 'Sonsonate'),
        ('Izalco', 'Izalco'),
        ('Nahuizalco', 'Nahuizalco'),
        ('Acajutla', 'Acajutla'),
        ('Juayúa', 'Juayúa'),

        # Usulután
        ('Usulután', 'Usulután'),
        ('Jiquilisco', 'Jiquilisco'),
        ('Puerto El Triunfo', 'Puerto El Triunfo'),
        ('Santiago de María', 'Santiago de María'),
        ('Santa Elena', 'Santa Elena'),
    ]

class CustomDateInput(DateInput):
    input_type = 'date'
    format = '%Y-%m-%d'

    def __init__(self, attrs=None):
        final_attrs = {'class': 'table__left__information__form__new__block-input'}
        if attrs:
            final_attrs.update(attrs)
        super().__init__(attrs=final_attrs, format=self.format)


# General -> Administracion

class RolForm(forms.ModelForm):
    comentarios = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={
            'class': 'table__left__information__form__new__block-textarea',
            'placeholder': 'Ingrese comentarios...',
        })
    )

    class Meta:
        model = Rol
        fields = ['nombre', 'tipo_rol', 'estado', 'comentarios']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'table__left__information__form__new__block-input',
                'placeholder': 'Nuevo rol',
            }),
            'tipo_rol': forms.Select(attrs={
                'class': 'table__left__information__form__new__block-input',
            }),
            'estado': forms.Select(attrs={
                'class': 'table__left__information__form__new__block-input',
            }),
        }

class PermisoForm(forms.ModelForm):
    comentarios = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={
            'class': 'table__left__information__form__new__block-textarea',
            'placeholder': 'Ingrese comentarios...',
        })
    )

    class Meta:
        model = Permiso
        fields = ['nombre', 'estado', 'comentarios']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'table__left__information__form__new__block-input',
                'placeholder': 'Nuevo permiso',
            }),
            'estado': forms.Select(attrs={
                'class': 'table__left__information__form__new__block-input',
            }),
        }

class AsignarPermisoForm(forms.ModelForm):
    permisos = forms.ModelMultipleChoiceField(
        queryset=Permiso.objects.filter(estado='ACTIVO'),
        widget=forms.SelectMultiple(attrs={
            'class': 'table__left__information__form__new__block-input',
            'size': '8'
        }),
        required=True,
        label="Permisos"
    )


    class Meta:
        model = AsignarPermiso
        fields = ['rol', 'permisos']
        widgets = {
            'rol': forms.Select(attrs={
                'class': 'table__left__information__form__new__block-input',
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filtrar solo roles activos
        self.fields['rol'].queryset = self.fields['rol'].queryset.filter(estado='ACTIVO')

class UsuarioForm(forms.ModelForm):
    contraseña = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'table__left__information__form__new__block-input',
            'placeholder': 'Ingrese contraseña',
        }),
        required=False,
        label='Contraseña'
    )

    class Meta:
        model = Usuario
        fields = ['nombre', 'usuario', 'contraseña', 'telefono', 'email', 'estado', 'rol']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'table__left__information__form__new__block-input',                 'placeholder': 'Nombre del usuario'}),
            'usuario': forms.TextInput(attrs={'class': 'table__left__information__form__new__block-input', 'placeholder': 'Usuario'}),
            'telefono': forms.TextInput(attrs={'class': 'table__left__information__form__new__block-input', 'placeholder': 'Telefono movil'}),
            'email': forms.EmailInput(attrs={'class': 'table__left__information__form__new__block-input', 'placeholder': 'Correo electronico'}),
            'estado': forms.Select(attrs={'class': 'table__left__information__form__new__block-input'}),
            'rol': forms.Select(attrs={'class': 'table__left__information__form__new__block-input'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Filtrar roles activos
        self.fields['rol'].queryset = Rol.objects.filter(estado='ACTIVO')

        if not self.instance.pk:
            self.fields['contraseña'].required = True
        else:
            # Cambiar el placeholder si se está editando
            self.fields['contraseña'].widget.attrs['placeholder'] = 'Llenar campo si desea cambiar la contraseña ...'

    def clean_contraseña(self):
        password = self.cleaned_data.get('contraseña')
        if password:
            return make_password(password)
        return self.instance.contraseña

# Modulos -> Empleados 

class CargoForm(forms.ModelForm):
    comentarios = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={
            'class': 'table__left__information__form__new__block-textarea',
            'placeholder': 'Ingrese comentarios...',
        }),
        label='Comentarios'
    )

    class Meta:
        model = Cargo
        fields = ['nombre', 'estado', 'comentarios']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'table__left__information__form__new__block-input',
                'placeholder': 'Nombre del cargo',
            }),
            'estado': forms.Select(attrs={
                'class': 'table__left__information__form__new__block-input',
            }),
        }

class EmpleadoForm(forms.ModelForm):
    nacionalidad = forms.ChoiceField(choices=[])
    departamento = forms.ChoiceField(choices=[])
    municipio = forms.ChoiceField(choices=[])

    comentarios = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={
            'class': 'table__left__information__form__new__block-textarea table__left__information__form__new__block-textarea-small',
            'placeholder': 'Ingrese comentarios...',
        }),
        label='Comentarios'
    )

    class Meta:
        model = Empleado
        fields = [
            'nombre', 'fecha_nacimiento', 'sexo', 'telefono', 'dui',
            'tipo_cargo', 'nit', 'tipo_pago', 'afp', 'salario', 'seguro', 'fecha_ingreso', 'nacionalidad',
            'fecha_salida', 'departamento', 'estado', 'municipio', 'eventual', 'domicilio', 'comentarios'
        ]
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'table__left__information__form__new__block-input', 'placeholder': 'Nombre completo'}),
            'fecha_nacimiento': CustomDateInput(attrs={'class': 'table__left__information__form__new__block-input'}),
            'domicilio': forms.Textarea(attrs={'class': 'table__left__information__form__new__block-textarea table__left__information__form__new__block-textarea-small', 'placeholder': 'Dirección exacta'}),
            'telefono': forms.TextInput(attrs={'class': 'table__left__information__form__new__block-input', 'placeholder': 'Número de teléfono'}),
            'sexo': forms.Select(attrs={'class': 'table__left__information__form__new__block-input'}),
            'dui': forms.TextInput(attrs={'class': 'table__left__information__form__new__block-input', 'placeholder': '00000000-0'}),
            'seguro': forms.TextInput(attrs={'class': 'table__left__information__form__new__block-input', 'placeholder': 'Número de seguro'}),
            'afp': forms.TextInput(attrs={'class': 'table__left__information__form__new__block-input', 'placeholder': 'Nombre o número de AFP'}),
            'nit': forms.TextInput(attrs={'class': 'table__left__information__form__new__block-input', 'placeholder': '0000-000000-000-0'}),
            'fecha_ingreso': CustomDateInput(attrs={'class': 'table__left__information__form__new__block-input'}),
            'fecha_salida': CustomDateInput(attrs={'class': 'table__left__information__form__new__block-input'}),
            'salario': forms.NumberInput(attrs={'class': 'table__left__information__form__new__block-input', 'placeholder': 'Monto mensual'}),
            'tipo_cargo': forms.Select(attrs={'class': 'table__left__information__form__new__block-input'}),
            'estado': forms.Select(attrs={'class': 'table__left__information__form__new__block-input'}),
            'tipo_pago': forms.Select(attrs={'class': 'table__left__information__form__new__block-input'}),
            'eventual': forms.Select(attrs={'class': 'table__left__information__form__new__block-input'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['nacionalidad'].choices = obtener_paises()
        self.fields['departamento'].choices = obtener_departamentos()
        self.fields['municipio'].choices = obtener_municipios()

        # Función para añadir clase sin borrar otras existentes
        def add_css_class(field_name, css_class):
            field = self.fields.get(field_name)
            if field:
                existing_classes = field.widget.attrs.get('class', '')
                clases = existing_classes.split()
                if css_class not in clases:
                    clases.append(css_class)
                    field.widget.attrs['class'] = ' '.join(clases)

        # Añadir la clase CSS necesaria para selects
        for field_name in ['nacionalidad', 'departamento', 'municipio']:
            add_css_class(field_name, 'table__left__information__form__new__block-input')

        self.fields['tipo_cargo'].queryset = Cargo.objects.filter(estado='ACTIVO')

        # Añadir clase extra a los textarea
        for field_name in ['domicilio', 'comentarios']:
            add_css_class(field_name, 'table__left__information__form__new__block-textarea-small')

# Modulos -> Permisos 

class TipoPermisoForm(forms.ModelForm):
    class Meta:
        model = TipoPermiso
        fields = ['nombre', 'estado']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'table__left__information__form__new__block-input',
                'placeholder': 'Nombre del tipo de permiso',
            }),
            'estado': forms.Select(attrs={
                'class': 'table__left__information__form__new__block-input',
            }),
        }

class PermisosForm(forms.ModelForm):
    comentarios = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'table__left__information__form__new__block-textarea table__left__information__form__new__block-textarea-small',
            'placeholder': 'Comentarios adicionales',
        }),
        label='Comentarios'
    )

    remuneracion = forms.ChoiceField(
        choices=[('SI', 'Sí'), ('NO', 'No')],
        widget=forms.Select(attrs={
            'class': 'table__left__information__form__new__block-input',  # misma clase que usas para selects en tus forms
        }),
        label='Remuneración'
    )

    class Meta:
        model = Permisos
        fields = ['empleado', 'fecha_inicio', 'fecha_fin', 'tipo_permiso', 'remuneracion', 'comentarios']
        widgets = {
            'empleado': forms.Select(attrs={
                'class': 'table__left__information__form__new__block-input',
            }),
            'fecha_inicio': CustomDateInput(attrs={
                'class': 'table__left__information__form__new__block-input',
            }),
            'fecha_fin': CustomDateInput(attrs={
                'class': 'table__left__information__form__new__block-input',
            }),
            'tipo_permiso': forms.Select(attrs={
                'class': 'table__left__information__form__new__block-input',
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filtrar solo empleados activos
        self.fields['empleado'].queryset = self.fields['empleado'].queryset.filter(estado='ACTIVO')
        # Filtrar solo tipos de permiso activos
        self.fields['tipo_permiso'].queryset = self.fields['tipo_permiso'].queryset.filter(estado='ACTIVO')