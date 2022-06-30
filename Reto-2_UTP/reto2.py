# id_cliente = int
# nombre = str
# edad = int
# primer_ingreso = boolean

# Funcion que identifica si el cliente es nuevo o no y si cumple con la edad
def cliente(informacion: dict) -> dict:
    if informacion['edad'] >= 18:
        atraccionN = 'X-Treme'
        aptoN = True
        altura_min = 120  # cm
        if informacion['primer_ingreso'] == True:
            Descuento = 0.05
            descuentoPrecioBoleta = (20000*Descuento)
            precioBoleta = 20000 - descuentoPrecioBoleta
        else:
            precioBoleta = 20000

    elif informacion['edad'] >= 15 and informacion['edad'] <= 18:
        atraccionN = 'Carros chocones'
        aptoN = True
        altura_min = 100  # cm
        if informacion['primer_ingreso'] == True:
            Descuento = 0.07
            descuentoPrecioBoleta = (5000*Descuento)
            precioBoleta = 5000 - descuentoPrecioBoleta
        else:
            precioBoleta = 5000

    elif informacion['edad'] >= 7 and informacion['edad'] < 15:
        atraccionN = 'Sillas voladoras'
        aptoN = True
        altura_min = 90  # cm
        if informacion['primer_ingreso'] == True:
            Descuento = 0.05
            descuentoPrecioBoleta = (10000*Descuento)
            precioBoleta = 10000 - descuentoPrecioBoleta
        else:
            precioBoleta = 10000
    else:
        atraccionN = 'N/A'
        precioBoleta = 'N/A'
        aptoN = False
        altura_min = 'N/A'  # cm

    dicSalida = {
        'nombre': informacion['nombre'],
        'edad': informacion['edad'],
        'atraccion': atraccionN,
        'apto': aptoN,
        'primer_ingreso': informacion['primer_ingreso'],
        'total_boleta': precioBoleta,
        'altura_min': altura_min
    }
    return dicSalida


# Diccionario de entrada, esto no se sube al Imaster
informacion = {
    'id_cliente': 1,
    'nombre': 'Johana Fernandez',
    'edad': 20,
    'primer_ingreso': True
}

print(cliente(informacion))
print(cliente({'nombre': 'Johana Fernandez',
      'edad': 20, 'primer_ingreso': False}))
print(cliente({'nombre': 'Gloria Suarez', 'edad': 3, 'primer_ingreso': True}))
print(cliente({'nombre': 'Gloria Suarez', 'edad': 3, 'primer_ingreso': False}))
print(cliente({'nombre': 'Tatiana Suarez ',
      'edad': 17, 'primer_ingreso': True}))
print(cliente({'nombre': 'Tatiana Suarez ',
      'edad': 17, 'primer_ingreso': False}))
print(cliente({'nombre': 'Tatiana Ruiz ', 'edad': 8, 'primer_ingreso': False}))
print(cliente({'nombre': 'Tatiana Ruiz ', 'edad': 8, 'primer_ingreso': True}))
