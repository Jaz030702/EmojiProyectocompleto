# Decisiones de Diseño

## 1. Arquitectura modular

El sistema fue dividido en múltiples archivos para separar responsabilidades:

- main.py  
  Punto de entrada del programa.

- ui.py  
  Maneja la interfaz gráfica.

- compiler.py  
  Implementa la lógica del compilador.

- symbols.py  
  Contiene la tabla de símbolos y reglas semánticas.

Esta separación mejora mantenibilidad y escalabilidad.

---

## 2. Uso de Tkinter

Se eligió Tkinter porque:

- Está incluido en Python
- Es simple de implementar
- Permite crear interfaces gráficas rápidamente
- No requiere dependencias externas

---

## 3. Diseño basado en compiladores reales

El proyecto sigue las etapas clásicas de compilación:

### Análisis léxico
Convierte texto en tokens.

### Análisis sintáctico
Valida la estructura de la oración.

### Análisis semántico
Verifica coherencia lógica.

### Generación de código objeto
Traduce tokens a emojis.

---

## 4. Tabla de símbolos

Se implementó una tabla hash (diccionario Python) por eficiencia.

Ventajas:

- Búsqueda rápida O(1)
- Fácil expansión
- Organización clara

---

## 5. Restricción gramatical

Se definió una gramática simple:

ORACION → SUJETO COMPLEMENTO

Esto facilita:

- Validación
- Detección de errores
- Escalabilidad futura

---

## 6. Manejo de errores

Se separaron tres tipos de errores:

### Error de entrada vacía
Cuando no se proporciona texto.

### Error sintáctico
Cuando la estructura es inválida.

### Error semántico
Cuando la oración no tiene sentido lógico.

---

## 7. Traducción directa a emojis

Cada palabra válida está asociada a:

- Tipo semántico
- Representación emoji

Esto permite conversión eficiente.

---

## 8. Escalabilidad

El sistema permite agregar fácilmente:

- Nuevos sujetos
- Nuevas categorías
- Más emojis
- Reglas semánticas adicionales