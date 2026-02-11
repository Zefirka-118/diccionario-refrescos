#Esto sera un diccionario de refrescos con sus respectivos identificadores (ID)
try:
    def buscar_refresco_por_id(refrescos, id_buscar):
        if id_buscar in refrescos:
            return refrescos[id_buscar]
        else:
            return "Refresco no encontrado."
       

    """Definimos un diccionario con algunos refrescos y sus IDs correspondientes"""
    refrescos = {
        1 : "Coca-Cola",
        2 : "Coca-Cola Light",
        3 : "Coca-Cola Zero",
        4 : "Pepsi",
        5 : "Fanta Naranja",
        6 : "Fanta Limón",
        7 : "Fanta Uva",
        8 : "Peñafiel mineral water",
        9 : "Peñaifel limón",
        10 : "Peñafiel naranja",
        11 : "Peñafiel toronja",
        12 : "Peñafiel uva",
        13 : "peñafiel mandarina",
        14 : "7up",
        15: "Mirinda",
        16 : "Sprite",
        17 : "Sangría",
        18 : "Topo Chico",
        19 : "Jarritos",
        20: "Vita"
}

    #Manual de uso
    id_buscar = int(input("Ingrese el ID del refresco que desea buscar (1-20):"))
    refresco_encontrado = buscar_refresco_por_id(refrescos, id_buscar)
    print(f"Refresco encontrado: {refresco_encontrado}")

except ValueError:
    print("Por favor, ingrese un número válido.")
except Exception:
    print("Ha ocurrido un error inesperado.")
