# Avance 4: Codificación e Implementación del Sistema

**Autores:** Bladimir Ferney Bermúdez Toloza & Darwin Samuel Machuca González

## 1. Estructura del Código
Se completó la implementación del software en Python respetando de forma estricta la arquitectura de tres (3) capas y el paradigma de Programación Estructurada:

* **Capa de Datos (`Codigo/datos.py`):** Contiene la lógica necesaria para interactuar exclusivamente con el archivo de texto plano `inspecciones.txt`, implementando funciones de lectura (`obtener_todos_los_registros`) y escritura (`guardar_registro`).
* **Capa Lógica (`Codigo/logica.py`):** Módulo encargado de procesar las inspecciones, calcular la densidad de cobertura vegetal (árboles por unidad de área) y formatear las muestras botánicas recolectadas.
* **Capa de Presentación (`Codigo/main.py`):** Interfaz basada en consola con un menú interactivo para capturar datos y mostrar los reportes de consulta.

Todo el código fuente funcional se encuentra alojado y organizado en la carpeta `/Codigo` de este repositorio.
