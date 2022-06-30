informacion = {
    'id_cliente': 4,
    'nombre': 'Tatiana Ruiz',
    'edad': 19,
    'primer_ingreso': False,
}


def cliente(informacion: dict) -> dict:
    edad = informacion['edad']
    valor_boleta = 'N/A'
    atraccion = 'N/A'
    apto = False
    if edad > 18:
        valor_boleta = 20000
        atraccion = 'X-Treme'
        apto = True
        if informacion['primer_ingreso'] == True:
            valor_boleta = valor_boleta-(valor_boleta*0.05)

    if edad >= 15 and edad <= 18:
        valor_boleta = 5000
        atraccion = 'Carros chocones'
        apto = True
        if informacion['primer_ingreso'] == True:
            valor_boleta = valor_boleta-(valor_boleta*0.07)

    if edad >= 7 and edad < 15:
        valor_boleta = 10000
        atraccion = 'Sillas voladoras'
        apto = True
        if informacion['primer_ingreso'] == True:
            valor_boleta = valor_boleta-(valor_boleta*0.05)

    respuesta = {
        'nombre': informacion['nombre'],
        'edad': edad,
        'atraccion': atraccion,
        'apto': apto,
        'primer_ingreso': informacion['primer_ingreso'],
        'total_boleta': valor_boleta
    }
    return respuesta


print(cliente(informacion))
print(cliente({'nombre': 'Juan', 'edad': 3, 'primer_ingreso': True}))
