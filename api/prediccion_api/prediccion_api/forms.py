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
        ('urgente', 'Urgente'),
        ('programado', 'Programado'),
        ('traslado', 'Traslado'),
    ]
    
    SERVICIO_ALTA_CHOICES = [
        ('', 'Seleccione...'),
        ('medicina_interna', 'Medicina Interna'),
        ('cirugia', 'Cirugía'),
        ('pediatria', 'Pediatría'),
        ('ginecologia', 'Ginecología'),
        ('traumatologia', 'Traumatología'),
        ('cardiologia', 'Cardiología'),
        ('neurologia', 'Neurología'),
        ('otro', 'Otro'),
    ]
    
    SITUACION_ALTA_CHOICES = [
        ('', 'Seleccione...'),
        ('alta_medica', 'Alta médica'),
        ('traslado', 'Traslado'),
        ('defuncion', 'Defunción'),
        ('alta_voluntaria', 'Alta voluntaria'),
    ]
    
    ESTANCIA_GRUPO_CHOICES = [
        ('', 'Seleccione...'),
        ('corta', 'Corta (1-3 días)'),
        ('media', 'Media (4-7 días)'),
        ('larga', 'Larga (8+ días)'),
    ]
    
    UCI_GRUPO_CHOICES = [
        ('', 'Seleccione...'),
        ('sin_uci', 'Sin UCI'),
        ('uci_corta', 'UCI Corta (1-2 días)'),
        ('uci_larga', 'UCI Larga (3+ días)'),
    ]
    
    SINO_CHOICES = [
        ('', 'Seleccione...'),
        ('si', 'Sí'),
        ('no', 'No'),
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
    
    dx_principal = forms.CharField(
        label='Dx principal de egreso .1',
        max_length=200,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese el diagnóstico principal'
        })
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
        choices=SINO_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    tiene_procedimiento = forms.ChoiceField(
        label='Tiene_procedimiento',
        choices=SINO_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
 