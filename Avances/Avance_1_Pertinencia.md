# Avance 1: Planteamiento y Arquitectura del Sistema

**Proyecto:** Software de Soporte - Inventario Forestal Nacional (IFN) del IDEAM
**Materia:** Programación I (Trabajo Final de Semestre)

### Integrantes
* **Bladimir Ferney Bermúdez Toloza** - 01251152013
* **Darwin Samuel Machuca González** - 01251152024

---

## 1. Pertinencia del Desarrollo

Para el desarrollo de este proyecto, nos vamos a basar estrictamente en el paradigma de **Programación Estructurada**. El objetivo es crear un software que ayude a gestionar el Inventario Forestal Nacional del IDEAM, pero asegurándonos de usar únicamente las técnicas y herramientas vistas durante el curso. 

Por lo tanto, todo el código estará construido a partir de funciones modulares, ciclos, condicionales y estructuras de datos básicas (como listas y diccionarios). No utilizaremos librerías externas ni tecnologías avanzadas que puedan invalidar la entrega.

## 2. Requisitos a Cumplir

Según el planteamiento del caso, el sistema debe resolver los siguientes puntos clave:

* **Registro y Consulta:** El programa debe permitir guardar y luego consultar las inspecciones de los conglomerados. Al buscar, debe mostrar la brigada encargada, el área y el conteo de las especies muestreadas.
* **Cálculos Matemáticos:** Se debe procesar la información recolectada para calcular métricas como la densidad de cobertura vegetal (total de árboles divididos por el área).
* **Interfaz de Usuario:** Toda la interacción se hará mediante un menú en la consola.
* **Persistencia de Datos:** Toda la información recolectada por las brigadas se tiene que guardar de forma permanente utilizando archivos de texto plano.
* **Estructura del Código:** Es obligatorio separar el proyecto usando una arquitectura de tres (3) capas.

## 3. Diseño de la Arquitectura (3 Capas)

Para cumplir con la arquitectura exigida y mantener el código ordenado, vamos a dividir el proyecto en tres módulos o archivos de Python independientes:

1. **Capa de Presentación (`main.py`):** Este archivo manejará exclusivamente los menús y la interacción por consola. Se encarga de pedir los datos al usuario (ID del conglomerado, cantidad de árboles, muestras, etc.) y de imprimir los resultados en pantalla. No hará cálculos ni guardará archivos.
2. **Capa Lógica (`logica.py`):** Es el "cerebro" del programa. Recibe los datos que capturó el `main.py`, ejecuta operaciones matemáticas como el cálculo de la densidad, y organiza la información de las muestras en un formato adecuado para poder guardarlas.
3. **Capa de Datos (`datos.py`):** Este será el único módulo con autorización para interactuar con los archivos. Solo contendrá funciones para abrir, escribir y leer el archivo de texto plano (`inspecciones.txt`), garantizando la persistencia de la información.
