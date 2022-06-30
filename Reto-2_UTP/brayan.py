def cliente(informacion: dict) -> dict:
    valor_boleta = 'N/A'
    atraccion = 'N/A'
    apto = False
    edad = informacion['edad']

    if edad > 18:
        valor_boleta = 20000
        atraccion = 'X-Treme'
        apto = True
        if informacion['primer_ingreso'] == True:
            valor_boleta = valor_boleta - (valor_boleta * 0.05)

    elif edad >= 15 and edad <= 18:
        valor_boleta = 5000
        atraccion = 'Carros chocones'
        apto = True
        if informacion['primer_ingreso'] == True:
            valor_boleta = valor_boleta - (valor_boleta * 0.07)

    elif edad >= 7 and edad < 15:
        valor_boleta = 10000
        atraccion = 'Sillas voladoras'
        apto = True
        if informacion['primer_ingreso'] == True:
            valor_boleta = valor_boleta - (valor_boleta * 0.05)

    diccionario = {
        'nombre': informacion['nombre'],
        'edad': edad,
        'atraccion': atraccion,
        'apto': apto,
        'primer_ingreso': informacion['primer_ingreso'],
        'total_boleta': valor_boleta
    }
    return diccionario


diccionario = {
    'id_cliente': 1,
    'nombre': 'Johana Fernandez',
    'edad': 3,
    'primer_ingreso': True
}
print(cliente(diccionario))
print(cliente({'nombre': 'Juan', 'edad': 19, 'primer_ingreso': True}))
print(cliente({'nombre': 'Juan', 'edad': 17, 'primer_ingreso': True}))
print(cliente({'nombre': 'Juan', 'edad': 14, 'primer_ingreso': False}))
