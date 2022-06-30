def cliente(informacion: dict):
    if informacion['edad'] > 18 and informacion['primer_ingreso'] == True:
        descuento = 20000 * 0.05
        informacion['total_boleta'] = 20000 - descuento
        informacion['apto'] = True
        informacion = {'nombre': informacion['nombre'], 'edad': informacion['edad'], 'atraccion': 'X-Treme',
                       'apto': informacion['apto'], 'primer_ingreso': informacion['primer_ingreso'], 'total_boleta': informacion['total_boleta']}
        return informacion
    if informacion['edad'] > 18 and informacion['primer_ingreso'] == False:
        informacion['total_boleta'] = 20000
        informacion['apto'] = True
        informacion = {'nombre': informacion['nombre'], 'edad': informacion['edad'], 'atraccion': 'X-Treme',
                       'apto': informacion['apto'], 'primer_ingreso': informacion['primer_ingreso'], 'total_boleta': informacion['total_boleta']}
        return informacion

    if informacion['edad'] >= 15 and informacion['edad'] <= 18 and informacion['primer_ingreso'] == True:
        descuento = 5000 * 0.07
        informacion['total_boleta'] = 5000 - descuento
        informacion['apto'] = True
        informacion = {'nombre': informacion['nombre'], 'edad': informacion['edad'], 'atraccion': 'Carros chocones',
                       'apto': informacion['apto'], 'primer_ingreso': informacion['primer_ingreso'], 'total_boleta': informacion['total_boleta']}
        return informacion
    if informacion['edad'] >= 15 and informacion['edad'] <= 18 and informacion['primer_ingreso'] == False:
        informacion['total_boleta'] = 5000
        informacion['apto'] = True
        informacion = {'nombre': informacion['nombre'], 'edad': informacion['edad'], 'atraccion': 'Carros chocones',
                       'apto': informacion['apto'], 'primer_ingreso': informacion['primer_ingreso'], 'total_boleta': informacion['total_boleta']}
        return informacion

    if informacion['edad'] >= 7 and informacion['edad'] < 15 and informacion['primer_ingreso'] == True:
        descuento = 10000 * 0.05
        informacion['total_boleta'] = 10000 - descuento
        informacion['apto'] = True
        informacion = {'nombre': informacion['nombre'], 'edad': informacion['edad'], 'atraccion': 'Sillas voladoras',
                       'apto': informacion['apto'], 'primer_ingreso': informacion['primer_ingreso'], 'total_boleta': informacion['total_boleta']}
        return informacion
    if informacion['edad'] >= 7 and informacion['edad'] < 15 and informacion['primer_ingreso'] == False:
        informacion['total_boleta'] = 10000
        informacion['apto'] = True
        informacion = {'nombre': informacion['nombre'], 'edad': informacion['edad'], 'atraccion': 'Sillas voladoras',
                       'apto': informacion['apto'], 'primer_ingreso': informacion['primer_ingreso'], 'total_boleta': informacion['total_boleta']}
        return informacion
    if informacion['edad'] < 7:
        informacion['atraccion'] = 'N/A'
        informacion['total_boleta'] = 'N/A'
        informacion['apto'] = False
        informacion = {'nombre': informacion['nombre'], 'edad': informacion['edad'], 'atraccion': 'N/A',
                       'apto': informacion['apto'], 'primer_ingreso': informacion['primer_ingreso'], 'total_boleta': informacion['total_boleta']}
        return informacion

    dicSalida = {
        'nombre': informacion['nombre'],
        'edad': informacion['edad'],
        'atraccion': atraccion,
        'apto': apto,
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
