# Autores: Bladimir Ferney Bermúdez Toloza (01251152013) & Darwin Samuel Machuca González (01251152024)
ARCHIVO_DATOS = "inspecciones.txt"

def guardar_registro(linea_datos):
    archivo = open(ARCHIVO_DATOS, "a", encoding="utf-8")
    archivo.write(linea_datos + "\n")
    archivo.close()

def obtener_todos_los_registros():
    try:
        archivo = open(ARCHIVO_DATOS, "r", encoding="utf-8")
        lineas = archivo.readlines()
        archivo.close()
        return lineas
    except FileNotFoundError:
        return []
