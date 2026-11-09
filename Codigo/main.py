import logica

def opcion_registrar():
    print("\n--- REGISTRO DE INSPECCIÓN ---")
    conglomerado = input("ID del Conglomerado: ")
    area = float(input("Área (Hectáreas): "))
    brigada = input("Brigada: ")
    fustales = int(input("Cantidad de Fustales: "))
    latizales = int(input("Cantidad de Latizales: "))
    brinzales = int(input("Cantidad de Brinzales: "))
    
    cantidad_muestras = int(input("¿Cuántas muestras se tomaron?: "))
    muestras = []
    for i in range(cantidad_muestras):
        muestras.append({
            "nombre": input(f"Nombre común (Muestra {i+1}): "),
            "uso": input("Uso (medicinal, alimenticio, maderable): "),
            "codigo": input("Código: ")
        })
        
    if logica.registrar_inspeccion(conglomerado, area, brigada, fustales, latizales, brinzales, muestras):
        print("¡Inspección registrada en texto plano!")

def opcion_consultar():
    id_busqueda = input("\nID del conglomerado a consultar: ")
    resultado = logica.buscar_inspeccion(id_busqueda)
    
    if resultado:
        print(f"\nConglomerado: {resultado['conglomerado']} | Brigada: {resultado['brigada']}")
        print(f"Densidad de cobertura: {resultado['densidad']} árboles/área")
        for m in resultado['muestras']:
            print(f" - [{m['codigo']}] {m['nombre']} ({m['uso']})")
    else:
        print("No se encontró el conglomerado.")

if __name__ == "__main__":
    while True:
        print("\n1. Registrar | 2. Consultar | 3. Salir")
        op = input("Opción: ")
        if op == '1': opcion_registrar()
        elif op == '2': opcion_consultar()
        elif op == '3': break
