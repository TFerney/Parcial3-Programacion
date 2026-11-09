# Avance 3: Prueba de Diseño (Prueba de Escritorio)

**Autores:** Bladimir Ferney Bermúdez Toloza & Darwin Samuel Machuca González

Se ejecuta una prueba de escritorio con un conjunto de datos controlado para verificar el correcto cálculo de la densidad de cobertura vegetal y el formateo de salida antes de la implementación.

## 1. Conjunto de Datos de Entrada
* **Conglomerado:** CONG-501
* **Área:** 2.0 (Hectáreas)
* **Brigada:** Brigada Bucaramanga
* **Fustales:** 120
* **Latizales:** 60
* **Brinzales:** 40
* **Muestras:** 1 (Nombre: Cedro, Uso: Maderable, Código: CED-01)

## 2. Ejecución de la Lógica Paso a Paso
1. `total_arboles` = 120 + 60 + 40 = 220 árboles.
2. `densidad` = 220 / 2.0 = **110.00 árboles/hectárea**.
3. `cadena_muestras` = "Cedro-Maderable-CED-01"

## 3. Salida Esperada en `inspecciones.txt`
`CONG-501,2.0,Brigada Bucaramanga,120,60,40,110.00,Cedro-Maderable-CED-01`

**Resultado:** El diseño algorítmico cumple con las especificaciones matemáticas del IDEAM.
