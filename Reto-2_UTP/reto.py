def cliente(informacion: dict):
    if informacion['edad'] > 18:
        atraccion = 'X-Treme'
        apto = True
        if informacion['primer_ingreso'] == True:
            descuento = 20000 * 0.05
            informacion['total_boleta'] = 20000 - descuento
        else:
            informacion['total_boleta'] = 20000

    if informacion['edad'] < 18:
        atraccion = 'Carros chocones'
        apto = True
        informacion['atraccion'] = 'N/A'
        informacion['total_boleta'] = 'N/A'

    if informacion['edad'] >= 15 and informacion['edad'] <= 18:
        atraccion = 'Carros chocones'
        apto = True
        if informacion['primer_ingreso'] == True:
            descuento = 5000 * 0.07
            informacion['total_boleta'] = 5000 - descuento
        else:
            informacion['total_boleta'] = 5000

    if informacion['edad'] < 15:
        atraccion = 'Sillas voladoras'
        apto = True
        informacion['atraccion'] = 'N/A'
        informacion['total_boleta'] = 'N/A'

    if informacion['edad'] >= 7 and informacion['edad'] < 15:
        atraccion = 'Sillas voladoras'
        apto = True
        if informacion['primer_ingreso'] == True:
            descuento = 10000 * 0.05
            informacion['total_boleta'] = 10000 - descuento

        else:
            informacion['total_boleta'] = 10000

    if informacion['edad'] < 7:
        informacion['atraccion'] = 'N/A'
        informacion['total_boleta'] = 'N/A'

    dicSalida = {
        'nombre': informacion['nombre'],
        'edad': informacion['edad'],
        'atraccion': atraccion,
        'apto': apto,
        'primer_ingreso': informacion['primer_ingreso'],
        'total_boleta': informacion['total_boleta']
    }
    return dicSalida


print(cliente({'nombre': 'Juan', 'edad': 20, 'primer_ingreso': True}))
print(cliente({'nombre': 'Pedro', 'edad': 10, 'primer_ingreso': False}))
print(cliente({'nombre': 'Maria', 'edad': 5, 'primer_ingreso': True}))
print(cliente({'nombre': 'Juana', 'edad': 17, 'primer_ingreso': False}))
print(cliente({'nombre': 'Juana', 'edad': 19, 'primer_ingreso': True}))
print(cliente({'nombre': 'Juana', 'edad': 3, 'primer_ingreso': False}))
