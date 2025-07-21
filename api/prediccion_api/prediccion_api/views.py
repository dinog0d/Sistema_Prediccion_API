from django.shortcuts import render
from django.http import HttpResponse
from .forms import PrediccionForm
from .modelo.modelo_xgboost import modelo_grd

def index(request):
    return HttpResponse("¡Hola mundo! API de predicción funcionando.")

def formulario_prediccion(request):
    if request.method == 'POST':
        form = PrediccionForm(request.POST)
        if form.is_valid():
            # Obtener todos los datos del formulario
            datos = {
                'grupo_edad': form.cleaned_data['grupo_edad'],
                'sexo': form.cleaned_data['sexo'],
                'tipo_ingreso': form.cleaned_data['tipo_ingreso'],
                'servicio_alta': form.cleaned_data['servicio_alta'],
                'cuidados_intensivos': form.cleaned_data['cuidados_intensivos'],
                'situacion_alta': form.cleaned_data['situacion_alta'],
                'dx_principal': form.cleaned_data['dx_principal'],
                'estancia_grupo': form.cleaned_data['estancia_grupo'],
                'uci_grupo': form.cleaned_data['uci_grupo'],
                'tiene_comorbilidad': form.cleaned_data['tiene_comorbilidad'],
                'tiene_procedimiento': form.cleaned_data['tiene_procedimiento'],
            }
            
            # Realizar predicción con el modelo XGBoost
            resultado_prediccion = modelo_grd.predecir(datos)
            
            # Mensaje de resultado
            if resultado_prediccion['error']:
                resultado = f"Error en la predicción: {resultado_prediccion['error']}"
            else:
                resultado = f"Predicción realizada exitosamente para paciente {datos['sexo']}, grupo de edad {datos['grupo_edad']}"
            
            return render(request, 'resultado.html', {
                'datos': datos,
                'resultado': resultado,
                'prediccion': resultado_prediccion
            })
        else:
            # Si el formulario tiene errores, mostrarlos
            print("Errores del formulario:", form.errors)  # Debug
            return render(request, 'formulario.html', {'form': form})
    else:
        form = PrediccionForm()
    
    return render(request, 'formulario.html', {'form': form})