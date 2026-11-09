# Avance 5: Prueba de Funcionalidad y Validación

**Autores:** Bladimir Ferney Bermúdez Toloza & Darwin Samuel Machuca González

## Evidencia de Funcionamiento por Consola

### 1. Caso de Prueba 1: Registro Exitoso
* **Entrada:** Conglomerado `CONG-101`, Área `5.0`, Brigada `Santander 1`, Fustales `200`, Latizales `100`, Brinzales `50`. Muestra: `Roble`, Uso: `Maderable`, Código: `ROB-01`.
* **Resultado:** Mensaje `¡Inspección registrada en texto plano!` desplegado en la consola.
* **Verificación:** El archivo `inspecciones.txt` almacena la línea:
  `CONG-101,5.0,Santander 1,200,100,50,70.00,Roble-Maderable-ROB-01`

### 2. Caso de Prueba 2: Consulta de Conglomerado
* **Entrada:** Búsqueda por ID `CONG-101`.
* **Resultado en Pantalla:**
  ```text
  Conglomerado: CONG-101 | Brigada: Santander 1
  Densidad de cobertura: 70.0 árboles/área
   - [ROB-01] Roble (Maderable)
