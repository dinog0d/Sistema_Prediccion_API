
# Sistema de Predicción de Códigos GRD

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Django](https://img.shields.io/badge/Django-4.x-green.svg)
![XGBoost](https://img.shields.io/badge/XGBoost-ML-orange.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 📋 Tabla de Contenidos

- [Descripción](#descripción)
- [Características](#características)
- [Tecnologías Utilizadas](#tecnologías-utilizadas)
- [Modelo de Machine Learning](#modelo-de-machine-learning)
- [Instalación](#instalación)
- [Uso](#uso)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [API Reference](#api-reference)
- [Contribución](#contribución)
- [Licencia](#licencia)

---

## 📖 Descripción

> Sistema web desarrollado en **Django** que utiliza **Machine Learning** para predecir **Códigos GRD (Grupos Relacionados de Diagnóstico)** basándose en datos clínicos y demográficos de pacientes hospitalarios.

El sistema automatiza la asignación de códigos GRD, reduciendo el tiempo de codificación manual y mejorando la precisión en la gestión hospitalaria.

---

## ✨ Características

- 🏥 **Interfaz web intuitiva** para captura de datos clínicos
- 🤖 **Predicción automática** de códigos GRD usando XGBoost
- 📊 **Visualización de confianza** con barras de progreso
- ✅ **Validación de formularios** en tiempo real
- 📱 **Diseño responsivo** con Bootstrap 5
- 🔄 **Selección múltiple** de comorbilidades y procedimientos
- 📈 **Métricas de confianza** para cada predicción

---

## 🛠️ Tecnologías Utilizadas

### Backend
| Tecnología | Versión | Propósito |
|------------|---------|-----------|
| **Django** | 4.x | Framework web principal |
| **Python** | 3.8+ | Lenguaje de programación |
| **XGBoost** | Latest | Algoritmo de Machine Learning |
| **scikit-learn** | Latest | Preprocesamiento de datos |
| **pandas** | Latest | Manipulación de datos |
| **joblib** | Latest | Serialización del modelo |

### Frontend
- **Bootstrap 5** - Framework CSS
- **HTML5/CSS3** - Estructura y estilos
- **JavaScript** - Interactividad

### Machine Learning
- **XGBoost Classifier** - Modelo principal
- **One-Hot Encoding** - Codificación categórica
- **Feature Engineering** - Procesamiento de características

---

## 🧠 Modelo de Machine Learning

### Algoritmo: XGBoost (Extreme Gradient Boosting)

#### ¿Por qué XGBoost?

✅ **Excelente rendimiento** en clasificación multiclase  
✅ **Manejo robusto** de características mixtas  
✅ **Resistente a overfitting**  
✅ **Alta precisión** en problemas médicos  

### Características del Modelo

#### Variables de Entrada (61 características):

| Categoría | Cantidad | Descripción |
|-----------|----------|-------------|
| **Demográficas** | 2 | Edad, Sexo |
| **Clínicas** | 7 | Diagnóstico principal, tipo ingreso, servicio alta, etc. |
| **Comorbilidades** | 36 | 1 general + 35 específicas (CIE-10) |
| **Procedimientos** | 21 | 1 general + 20 específicos |

**Autores**

Yuliana Selena Alzate Que Palacio

Dairon Alberto Montes Barrada

Julian Alejandro Olaya Posso
