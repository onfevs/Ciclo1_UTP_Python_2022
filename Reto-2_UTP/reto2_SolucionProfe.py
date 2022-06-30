"""
Apuntes

*Desarolle una funcion que reciba como parametro un diccionario
diccionario = {
    'id_cliente': 1,
    'nombre': 'Juan',
    'edad': 20,
    'primer_ingreso': True,
}

*La funcion debe retornar un diccionario con la siguiente estructura:

    respuesta ={
        'nombre' : "",
        'edad' : 0,
        'atraccion':""
        'primer_ingreso':True,
        'total_boleta':0
        'apto':True
    }

    *Apto es verdad solo si esta en el rango de edad de la tabla
    *Atraccion y total boleta N/A si no esta en el rango de edad de la tabla
    *Primer ingreso verdad, si es verdadero se aplica el descuento en la tabla
"""


def cliente(informacion: dict):
    # Obtengo la edad del cliente
    edad = informacion['edad']
    primer_ingreso = informacion['primer_ingreso']
    # Se declaran las variables por fuera de la funcion
    valor_boleta = "N/A"
    atraccion = "N/A"
    # Esto es una flag que si se declara en falso y dentro del if se pone true se enciende y se cambia a true.
    apto = False
    # Evaluar la edad del cliente
    if edad > 18:
        valor_boleta = 20000
        atraccion = "X-Treme"
        apto = True
        if primer_ingreso == True:
            valor_boleta = valor_boleta - (valor_boleta * 0.05)
    elif edad >= 15:
        valor_boleta = 5000
        atraccion = "Carros chocones"
        apto = True
        if primer_ingreso == True:
            valor_boleta = valor_boleta - (valor_boleta * 0.07)
    elif edad >= 7:
        valor_boleta = 10000
        atraccion = "Sillas voladoras"
        apto = True
        if primer_ingreso == True:
            valor_boleta = valor_boleta - (valor_boleta * 0.05)
    else:
        atraccion = "N/A"
        apto = False

    respuesta = {
        'nombre': informacion['nombre'],
        'edad': edad,
        'atraccion': atraccion,
        'primer_ingreso': informacion['primer_ingreso'],
        'apto': apto,
        'total_boleta': valor_boleta
    }
    return respuesta


print(cliente({'nombre': 'Juan', 'edad': 3, 'primer_ingreso': True}))
