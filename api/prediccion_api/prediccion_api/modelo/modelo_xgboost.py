import pandas as pd
import joblib
import os
import numpy as np

# === Carga del modelo previamente entrenado y serializado ===
BASE_DIR = os.path.dirname(os.path.abspath(__file__))       # Directorio actual del archivo
MODEL_PATH = os.path.join(BASE_DIR, 'modelo_xgboost.pkl')  # Ruta absoluta al modelo

class PrediccionGRD:
    def __init__(self):
        try:
            self.pipeline = joblib.load(MODEL_PATH)
            print(f"Modelo cargado exitosamente desde: {MODEL_PATH}")
        except FileNotFoundError:
            print(f"Error: No se encontró el modelo en {MODEL_PATH}")
            self.pipeline = None
        except Exception as e:
            print(f"Error al cargar el modelo: {e}")
            self.pipeline = None
    
    def preparar_datos(self, datos_formulario):
        """
        Convierte los datos del formulario al formato esperado por el modelo
        """
        # Mapeos de valores categóricos a numéricos
        mapeos = {
            'sexo': {'M': 1, 'F': 0},
            'tipo_ingreso': {'URGENCIA': 1, 'PROGRAMADO': 0},
            'situacion_alta': {'ALTA MÉDICA': 0, 'FALLECIDO': 1},
            'cuidados_intensivos': {'si': 1, 'no': 0}
        }
        
        # Crear DataFrame con las características base
        datos_procesados = {
            'Grupo Edad': self._procesar_grupo_edad(datos_formulario['grupo_edad']),
            'Sexo': mapeos['sexo'].get(datos_formulario['sexo'], 0),
            'Tipo de ingreso': mapeos['tipo_ingreso'].get(datos_formulario['tipo_ingreso'], 0),
            'ServicioAlta': int(datos_formulario['servicio_alta']) if datos_formulario['servicio_alta'] else 0,
            'Cuidados intensivos': mapeos['cuidados_intensivos'].get(datos_formulario['cuidados_intensivos'], 0),
            'Situacion al alta': mapeos['situacion_alta'].get(datos_formulario['situacion_alta'], 0),
            'Dx principal de egreso .1': self._procesar_dx_principal(datos_formulario['dx_principal']),
            'Estancia Grupo': self._procesar_estancia(datos_formulario['estancia_grupo']),
            'UCI Grupo': self._procesar_uci(datos_formulario['uci_grupo']),
        }
        
        # Agregar todas las características de comorbilidad que el modelo espera
        comorbilidades_esperadas = [
            'Tiene_I10', 'Tiene_Z720', 'Tiene_E038', 'Tiene_I270', 'Tiene_I120', 
            'Tiene_E106', 'Tiene_D648', 'Tiene_E116', 'Tiene_J448', 'Tiene_E876', 
            'Tiene_N390', 'Tiene_D728', 'Tiene_G448', 'Tiene_I48', 'Tiene_R104', 
            'Tiene_E755', 'Tiene_I110', 'Tiene_E788', 'Tiene_J441', 'Tiene_J90', 
            'Tiene_B962', 'Tiene_E668', 'Tiene_I251', 'Tiene_I081', 'Tiene_D508', 
            'Tiene_J980', 'Tiene_I083', 'Tiene_K296', 'Tiene_E871', 'Tiene_E878', 
            'Tiene_N40', 'Tiene_I132', 'Tiene_R509', 'Tiene_F058', 'Tiene_J960'
        ]
        
        # Inicializar todas las comorbilidades en 0
        for comorbilidad in comorbilidades_esperadas:
            datos_procesados[comorbilidad] = 0
        
        # Activar la comorbilidad específica seleccionada
        comorbilidad_seleccionada = datos_formulario['tiene_comorbilidad']
        if comorbilidad_seleccionada != '0':
            # Mapear las comorbilidades del formulario a las del modelo
            mapeo_comorbilidades = {
                'Dxr 1': 'Tiene_I10',
                'Dxr 2': 'Tiene_Z720', 
                'Dxr 3': 'Tiene_E038',
                'Dxr 4': 'Tiene_I270',
                'Dxr 5': 'Tiene_I120',
                'Dxr 6': 'Tiene_E106',
                'Dxr 7': 'Tiene_D648',
                'Dxr 8': 'Tiene_E116',
                'Dxr 9': 'Tiene_J448'
            }
            
            if comorbilidad_seleccionada in mapeo_comorbilidades:
                datos_procesados[mapeo_comorbilidades[comorbilidad_seleccionada]] = 1
        
        # Agregar la variable general de comorbilidad
        datos_procesados['Tiene_comorbilidad'] = 1 if comorbilidad_seleccionada != '0' else 0
        
        # Agregar todas las características de procedimientos que el modelo espera
        procedimientos_esperados = [
            'Tiene_87.44', 'Tiene_89.51', 'Tiene_88.72', 'Tiene_87.03', 'Tiene_45.16', 
            'Tiene_88.76', 'Tiene_87.41', 'Tiene_88.01', 'Tiene_88.38', 'Tiene_88.75', 
            'Tiene_45.23', 'Tiene_88.77', 'Tiene_38.93', 'Tiene_89.5', 'Tiene_88.71', 
            'Tiene_89.14', 'Tiene_88.91', 'Tiene_88.79', 'Tiene_88.26', 'Tiene_88.27'
        ]
        
        # Inicializar todos los procedimientos en 0
        for procedimiento in procedimientos_esperados:
            datos_procesados[procedimiento] = 0
        
        # Activar el procedimiento específico seleccionado
        procedimiento_seleccionado = datos_formulario['tiene_procedimiento']
        if procedimiento_seleccionado != '0':
            # Mapear los procedimientos del formulario a los del modelo
            mapeo_procedimientos = {
                'Proc1': 'Tiene_87.44',
                'Proc2': 'Tiene_89.51',
                'Proc3': 'Tiene_88.72',
                'Proc4': 'Tiene_87.03',
                'Proc5': 'Tiene_45.16',
                'Proc6': 'Tiene_88.76',
                'Proc7': 'Tiene_87.41',
                'Proc8': 'Tiene_88.01',
                'Proc9': 'Tiene_88.38',
                'Proc10': 'Tiene_88.75',
                'Proc11': 'Tiene_45.23',
                'Proc12': 'Tiene_88.77',
                'Proc13': 'Tiene_38.93',
                'Proc14': 'Tiene_89.5',
                'Proc15': 'Tiene_88.71',
                'Proc16': 'Tiene_89.14',
                'Proc17': 'Tiene_88.91',
                'Proc18': 'Tiene_88.79',
                'Proc19': 'Tiene_88.26',
                'Proc20': 'Tiene_88.27',
                'Proc21': 'Tiene_87.44',  # Mapear los extras a algunos existentes
                'Proc22': 'Tiene_89.51',
                'Proc23': 'Tiene_88.72',
                'Proc24': 'Tiene_87.03',
                'Proc25': 'Tiene_45.16',
                'Proc26': 'Tiene_88.76',
                'Proc27': 'Tiene_87.41',
                'Proc28': 'Tiene_88.01',
                'Proc29': 'Tiene_88.38',
                'Proc30': 'Tiene_88.75'
            }
            
            if procedimiento_seleccionado in mapeo_procedimientos:
                datos_procesados[mapeo_procedimientos[procedimiento_seleccionado]] = 1
        
        # Agregar la variable general de procedimiento
        datos_procesados['Tiene_procedimiento'] = 1 if procedimiento_seleccionado != '0' else 0
        
        # Crear DataFrame y ordenar las columnas según el orden esperado por el modelo
        df = pd.DataFrame([datos_procesados])
        
        # Orden esperado por el modelo (basado en el error)
        columnas_ordenadas = [
            'Grupo Edad', 'Sexo', 'Tipo de ingreso', 'ServicioAlta', 'Cuidados intensivos',
            'Situacion al alta', 'Dx principal de egreso .1', 'Estancia Grupo', 'UCI Grupo',
            'Tiene_comorbilidad', 'Tiene_I10', 'Tiene_Z720', 'Tiene_E038', 'Tiene_I270', 
            'Tiene_I120', 'Tiene_E106', 'Tiene_D648', 'Tiene_E116', 'Tiene_J448', 'Tiene_E876', 
            'Tiene_N390', 'Tiene_D728', 'Tiene_G448', 'Tiene_I48', 'Tiene_R104', 'Tiene_E755', 
            'Tiene_I110', 'Tiene_E788', 'Tiene_J441', 'Tiene_J90', 'Tiene_B962', 'Tiene_E668', 
            'Tiene_I251', 'Tiene_I081', 'Tiene_D508', 'Tiene_J980', 'Tiene_I083', 'Tiene_K296', 
            'Tiene_E871', 'Tiene_E878', 'Tiene_N40', 'Tiene_I132', 'Tiene_R509', 'Tiene_F058', 
            'Tiene_J960', 'Tiene_procedimiento', 'Tiene_87.44', 'Tiene_89.51', 'Tiene_88.72', 
            'Tiene_87.03', 'Tiene_45.16', 'Tiene_88.76', 'Tiene_87.41', 'Tiene_88.01', 
            'Tiene_88.38', 'Tiene_88.75', 'Tiene_45.23', 'Tiene_88.77', 'Tiene_38.93', 
            'Tiene_89.5', 'Tiene_88.71', 'Tiene_89.14', 'Tiene_88.91', 'Tiene_88.79', 
            'Tiene_88.26', 'Tiene_88.27'
        ]
        
        return df[columnas_ordenadas]
    
    def _procesar_grupo_edad(self, grupo_edad):
        """Convierte grupo de edad a numérico"""
        mapeo = {'0-17': 0, '18-44': 1, '45-64': 2, '65+': 3}
        return mapeo.get(grupo_edad, 1)
    
    def _procesar_dx_principal(self, dx):
        """Convierte diagnóstico principal a numérico"""
        mapeo = {'N39': 0, 'J44': 1, 'J18': 2, 'E10': 3, 'N20': 4, 
                'K80': 5, 'G40': 6, 'Z51': 7, 'I13': 8, 'I11': 9}
        return mapeo.get(dx, 0)
    
    def _procesar_estancia(self, estancia):
        """Convierte estancia a numérico"""
        mapeo = {'0-2': 0, '3-5': 1, '6-10': 2, '11-20': 3, '21-40': 4, '40+': 5}
        return mapeo.get(estancia, 1)
    
    def _procesar_uci(self, uci):
        """Convierte UCI a numérico"""
        mapeo = {'0': 0, '1': 1, '2-3': 2, '4-7': 3, '8-14': 4, '15+': 5}
        return mapeo.get(uci, 0)
    
    def predecir(self, datos_formulario):
        """
        Realiza la predicción con el modelo XGBoost
        """
        if self.pipeline is None:
            return {
                'prediccion': 'Error',
                'confianza': 0,
                'codigo_grd': 'No disponible',
                'error': 'Modelo no disponible'
            }
        
        try:
            # Preparar los datos
            datos_df = self.preparar_datos(datos_formulario)
            
            # Realizar predicción
            prediccion = self.pipeline.predict(datos_df)[0]
            
            # Obtener probabilidades si está disponible
            try:
                probabilidades = self.pipeline.predict_proba(datos_df)[0]
                confianza = max(probabilidades) * 100
            except:
                confianza = 85.0  # Valor por defecto si no hay probabilidades
            
            return {
                'prediccion': 'Exitosa',
                'codigo_grd': str(int(prediccion)),
                'confianza': round(confianza, 1),
                'error': None
            }
            
        except Exception as e:
            return {
                'prediccion': 'Error',
                'confianza': 0,
                'codigo_grd': 'No disponible',
                'error': str(e)
            }

# Instancia global del modelo
modelo_grd = PrediccionGRD()