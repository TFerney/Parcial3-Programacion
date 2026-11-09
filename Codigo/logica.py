import datos

def registrar_inspeccion(conglomerado, area, brigada, fustales, latizales, brinzales, muestras):
    total_arboles = fustales + latizales + brinzales
    densidad = total_arboles / area if area > 0 else 0.0
    
    muestras_formateadas = []
    for m in muestras:
        muestras_formateadas.append(f"{m['nombre']}-{m['uso']}-{m['codigo']}")
    cadena_muestras = "|".join(muestras_formateadas)
    
    linea = f"{conglomerado},{area},{brigada},{fustales},{latizales},{brinzales},{densidad:.2f},{cadena_muestras}"
    datos.guardar_registro(linea)
    return True

def buscar_inspeccion(id_conglomerado):
    registros = datos.obtener_todos_los_registros()
    for linea in registros:
        campos = linea.strip().split(',')
        if len(campos) >= 8 and campos[0] == id_conglomerado:
            muestras_brutas = campos[7].split('|') if campos[7] else []
            lista_muestras = [{"nombre": p.split('-')[0], "uso": p.split('-')[1], "codigo": p.split('-')[2]} for p in muestras_brutas if len(p.split('-')) == 3]
            return {
                "conglomerado": campos[0], "area": float(campos[1]), "brigada": campos[2],
                "fustales": int(campos[3]), "latizales": int(campos[4]), "brinzales": int(campos[5]),
                "densidad": float(campos[6]), "muestras": lista_muestras
            }
    return None
