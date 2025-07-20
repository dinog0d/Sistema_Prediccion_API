# Librerias necesarias
import pandas as pd
import joblib
import os

# === Carga del modelo previamente entrenado y serializado ===
BASE_DIR = os.path.dirname(os.path.abspath(__file__))       # Directorio actual del archivo
MODEL_PATH = os.path.join(BASE_DIR, 'modelo_xgboost.pkl')  # Ruta absoluta al modelo
pipeline = joblib.load(MODEL_PATH)                          # Cargar el modelo con joblib

mapeos = {}