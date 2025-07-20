from django.shortcuts import render
from django.http import HttpResponse
from .forms import PrediccionForm

def index(request):
    return HttpResponse("¡Hola mundo! API de predicción funcionando.")

def formulario_prediccion(request):
    if request.method == 'POST':
        form = PrediccionForm(request.POST)
        if form.is_valid():
            edad = form.cleaned_data['edad']
            sexo = form.cleaned_data['sexo']
            
            # Aquí puedes procesar los datos o hacer la predicción
            resultado = f"Datos recibidos - Edad: {edad}, Sexo: {'Masculino' if sexo == 'M' else 'Femenino'}"
            
            return render(request, 'resultado.html', {
                'resultado': resultado,
                'edad': edad,
                'sexo': sexo
            })
    else:
        form = PrediccionForm()
    
    return render(request, 'formulario.html', {'form': form})