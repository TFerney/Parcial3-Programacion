# Avance 2: Diseño de la Estructura (Algoritmo)

**Autores:** Bladimir Ferney Bermúdez Toloza & Darwin Samuel Machuca González

## 1. Explicación del Funcionamiento

El diseño del algoritmo sigue una arquitectura estructurada de tres capas:
1. **Presentación (Menú):** Muestra las opciones. Si el usuario elige registrar, captura los datos del conglomerado, conteo de árboles (fustales, latizales, brinzales) y las muestras botánicas.
2. **Lógica (Procesamiento):** Calcula el total de árboles y lo divide entre el área para hallar la **densidad de cobertura vegetal**. Luego, empaqueta todos los datos en una sola cadena de texto separada por comas.
3. **Datos (Persistencia):** Recibe la cadena formateada y la guarda en una nueva línea dentro de un archivo de texto plano (`inspecciones.txt`).

## 2. Pseudocódigo Estructurado (Módulo Lógico)

```text
INICIO FUNCION registrar_inspeccion(conglomerado, area, brigada, fustales, latizales, brinzales, muestras)
    // 1. Calcular indicadores
    total_arboles = fustales + latizales + brinzales
    
    SI area > 0 ENTONCES
        densidad = total_arboles / area
    SINO
        densidad = 0
    FIN SI
    
    // 2. Formatear muestras
    cadena_muestras = ""
    PARA CADA muestra EN muestras HACER
        cadena_muestras = cadena_muestras + muestra.nombre + "-" + muestra.uso + "|"
    FIN PARA
    
    // 3. Preparar registro para texto plano
    registro = conglomerado + "," + area + "," + brigada + "," + densidad + "," + cadena_muestras
    
    // 4. Llamar a capa de datos
    LLAMAR guardar_en_archivo("inspecciones.txt", registro)
    
    RETORNAR Verdadero
FIN FUNCION
