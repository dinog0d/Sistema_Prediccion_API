from django import forms

class PrediccionForm(forms.Form):
    # Opciones para los campos select
    GRUPO_EDAD_CHOICES = [
        ('', 'Seleccione...'),
        ('0-17', '0-17 años'),
        ('18-44', '18-44 años'),
        ('45-64', '45-64 años'),
        ('65+', '65+ años'),
    ]
    
    SEXO_CHOICES = [
        ('', 'Seleccione...'),
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    ]
    
    TIPO_INGRESO_CHOICES = [
        ('', 'Seleccione...'),
        ('URGENCIA', 'Urgencia'),
        ('PROGRAMADO', 'Programado'),
    ]
    
    SERVICIO_ALTA_CHOICES = [
        ('', 'Seleccione...'),
        (20, '20'),
        (21, '21'),
        (22, '22'),
        (23, '23'),
        (24, '24'),
        (25, '25'),
        (28, '28'),
        (29, '29'),
        (30, '30'),
        (31, '31'),
        (38, '38'),
        (39, '39'),
        (40, '40'),
        (42, '42'),
        (44, '44'),
        (45, '45'),
        (54, '54'),
        (55, '55'),
        (58, '58'),
        (59, '59'),
        (126, '126'),
        (156, '156'),
        (158, '158'),
        (162, '162'),
        (230, '230'),
        (297, '297'),
    ]
    
    SITUACION_ALTA_CHOICES = [
        ('', 'Seleccione...'),
        ('ALTA MÉDICA', 'Alta médica'),
        ('FALLECIDO', 'Fallecido'),
    ]
    
    ESTANCIA_GRUPO_CHOICES = [
        ('', 'Seleccione...'),
        ('0-2', '0-2 días'),
        ('3-5', '3-5 días'),
        ('6-10', '6-10 días'),
        ('11-20', '11-20 días'),
        ('21-40', '21-40 días'),
        ('40+', '40+ días'),
    ]
    
    UCI_GRUPO_CHOICES = [
        ('', 'Seleccione...'),
        ('0', '0 días (Sin UCI)'),
        ('1', '1 día'),
        ('2-3', '2-3 días'),
        ('4-7', '4-7 días'),
        ('8-14', '8-14 días'),
        ('15+', '15+ días'),
    ]
    
    PROCEDIMIENTO_CHOICES = [
        ('', 'Seleccione...'),
        (False, 'Sin procedimiento'),
        (True, 'Proc1'),
        (True, 'Proc2'),
        (True, 'Proc3'),
        (True, 'Proc4'),
        (True, 'Proc5'),
        (True, 'Proc6'),
        (True, 'Proc7'),
        (True, 'Proc8'),
        (True, 'Proc9'),
        (True, 'Proc10'),
        (True, 'Proc11'),
        (True, 'Proc12'),
        (True, 'Proc13'),
        (True, 'Proc14'),
        (True, 'Proc15'),
        (True, 'Proc16'),
        (True, 'Proc17'),
        (True, 'Proc18'),
        (True, 'Proc19'),
        (True, 'Proc20'),
        (True, 'Proc21'),
        (True, 'Proc22'),
        (True, 'Proc23'),
        (True, 'Proc24'),
        (True, 'Proc25'),
        (True, 'Proc26'),
        (True, 'Proc27'),
        (True, 'Proc28'),
        (True, 'Proc29'),
        (True, 'Proc30'),
    ]

    COMORBILIDAD_CHOICES = [
        ('', 'Seleccione...'),
        (False, 'Sin comorbilidad'),
        (True, 'Dxr 1'),
        (True, 'Dxr 2'),
        (True, 'Dxr 3'),
        (True, 'Dxr 4'),
        (True, 'Dxr 5'),
        (True, 'Dxr 6'),
        (True, 'Dxr 7'),
        (True, 'Dxr 8'),
        (True, 'Dxr 9'),
    ]

    SINO_CHOICES = [
        ('', 'Seleccione...'),
        (True, 'Sí'),
        (False, 'No'),
    ]

    DX_PPAL_CHOICES = [
        ('', 'Seleccione...'),
        ('N39', 'N39'),
        ('J44', 'J44'),
        ('J18', 'J18'),
        ('E10', 'E10'),
        ('N20', 'N20'),
        ('K80', 'K80'),
        ('G40', 'G40'),
        ('Z51', 'Z51'),
        ('I13', 'I13'),
        ('I11', 'I11'),
    ]


    
    # Campos del formulario
    grupo_edad = forms.ChoiceField(
        label='Grupo Edad',
        choices=GRUPO_EDAD_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    sexo = forms.ChoiceField(
        label='Sexo',
        choices=SEXO_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    tipo_ingreso = forms.ChoiceField(
        label='Tipo de ingreso',
        choices=TIPO_INGRESO_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    servicio_alta = forms.ChoiceField(
        label='ServicioAlta',
        choices=SERVICIO_ALTA_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    cuidados_intensivos = forms.ChoiceField(
        label='Cuidados intensivos',
        choices=SINO_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    situacion_alta = forms.ChoiceField(
        label='Situacion al alta',
        choices=SITUACION_ALTA_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    

    dx_principal = forms.ChoiceField(  
        label='Dx principal de egreso .1',
        choices=DX_PPAL_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    
    estancia_grupo = forms.ChoiceField(
        label='Estancia Grupo',
        choices=ESTANCIA_GRUPO_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    uci_grupo = forms.ChoiceField(
        label='UCI Grupo',
        choices=UCI_GRUPO_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    tiene_comorbilidad = forms.ChoiceField(
        label='comorbilidad',
        choices=COMORBILIDAD_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    tiene_procedimiento = forms.ChoiceField(
        label='Tiene_procedimiento',
        choices=PROCEDIMIENTO_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
 