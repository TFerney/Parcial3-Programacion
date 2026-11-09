# Sistema de Soporte al Inventario Forestal Nacional (IFN) — IDEAM

**Asignatura:** Programación I (Parcial 3 — Trabajo Final)  
**Institución:** Universidad de Santander (UDES)  
**Autores:** 
* Bladimir Ferney Bermúdez Toloza — Código: `01251152013
* Darwin Samuel Machuca González — Código: `01251152024`

---

##  Descripción del Proyecto

El presente proyecto consiste en un software en Python desarrollado para brindar soporte en campo a las brigadas del **Instituto de Hidrología, Meteorología y Estudios Ambientales (IDEAM)** dentro del marco del Inventario Forestal Nacional (IFN). 

La herramienta permite registrar las inspecciones realizadas en conglomerados boscosos, calcular indicadores ambientales clave como la **densidad de cobertura vegetal** y empaquetar información de muestras botánicas. Todo el desarrollo cumple de forma estricta con el paradigma de **Programación Estructurada** (uso exclusivo de funciones, condicionales, ciclos y estructuras de datos nativas sin librerías externas).

---

##  Arquitectura del Software (3 Capas)

El código fuente está organizado bajo una arquitectura modular de tres (3) capas para garantizar un bajo acoplamiento y facilitar el mantenimiento:

1. **Capa de Presentación (`Codigo/main.py`):**
   * Interfaz basada en consola interactiva por menús.
   * Captura y validación de datos de entrada del usuario.
2. **Capa Lógica (`Codigo/logica.py`):**
   * Procesamiento de reglas de negocio.
   * Cálculo de la densidad de cobertura vegetal mediante la fórmula:
     $$\text{Densidad} = \frac{\text{Fustales} + \text{Latizales} + \text{Brinzales}}{\text{Área (ha)}}$$
   * Formateo y empaquetado de muestras botánicas recolectadas.
3. **Capa de Datos (`Codigo/datos.py`):**
   * Persistencia permanente en el archivo plano `inspecciones.txt`.
   * Funciones dedicadas exclusivamente a la lectura y escritura en modo append (`'a'`).

---

## 📁 Estructura del Repositorio

```text
.
├── Codigo/
│   ├── datos.py       # Capa de almacenamiento y persistencia (.txt)
│   ├── logica.py      # Capa de negocio y cálculos matemáticos
│   └── main.py        # Capa de presentación e interfaz por consola
├── Avances/
│   ├── Avance_1_Pertinencia.md
│   ├── Avance_2_Diseno.md
│   ├── Avance_3_Prueba.md
│   ├── Avance_4_Implementacion.md
│   ├── Avance_5_Pruebas.md
│   └── Avance_6_Exposicion.md
└── README.md          # Documentación principal del proyecto
```

---

##  Instrucciones de Ejecución

### Prerrequisitos
* Tener instalado Python 3.x en el equipo.

### Ejecución por Consola
1. Clonar el repositorio o descargar el código fuente.
2. Abrir la terminal o línea de comandos en la carpeta raíz del proyecto.
3. Ejecutar el archivo de la capa de presentación:

```bash
python Codigo/main.py
```

---

##  Caso de Prueba (Validación)

* **Entrada:**
  * Conglomerado: `CONG-101` | Área: `2.5 ha` | Brigada: `Santander 1`
  * Conteos: `50` Fustales, `50` Latizales, `50` Brinzales.
  * Muestra Botánica: `Roble` (Uso: `Maderable`, Código: `ROB-01`).
* **Salida Calculada:**
  * Densidad de Cobertura: $60.0\text{ árboles/hectárea}$.
* **Registro en Texto Plano (`inspecciones.txt`):**
  ```text
  CONG-101,2.5,Santander 1,50,50,50,60.00,Roble-Maderable-ROB-01
  ```
