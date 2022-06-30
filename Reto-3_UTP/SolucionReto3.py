def AutoPartes(ventas: list):  # lista de tuplas
    diccionario = {}  # diccionario vacio
    for d in ventas:  # recorre la lista de tuplas
        if diccionario.get(d[0]) == None:  # si el diccionario no tiene el idProducto
            # separa la descripcion en partes
            diccionario[d[0]] = []  # agrega el idProducto al diccionario
        # agrega la tupla al diccionario
        diccionario[d[0]].append((d[1], d[2], d[3], d[4], d[5], d[6], d[7]))
    return diccionario  # retorna el diccionario


def consultaRegistro(ventas, idProducto):  # lista de tuplas, idProducto
    if idProducto in ventas:  # si el idProducto esta en la lista de tuplas
        for p in ventas[idProducto]:  # recorre la lista de tuplas
            print(
                f'Producto consultado : {idProducto} Descripción {p[0]} #Parte {p[1]} Cantidad vendida {p[2]} Stock {p[3]}  Comprador  {p[4]}  Documento {p[5]} Fecha Venta {p[6]}')  # imprime la tupla
    else:  # si el idProducto no esta en la lista de tuplas
        print('No hay registro de venta de ese producto')  # imprime mensaje


ventas = [
    (2001, 'rosca', 'PT29872', 2, 45, 'Luis Molero', 3456, '12/06/2020'),
    (2010, 'bujía', 'MS9512', 4, 15, 'Carlos Rondon', 1256, '12/06/2020'),
    (2010, 'bujía', 'ER6523', 9, 36, 'Pedro Montes', 1243, '12/06/2020'),
    (3578, 'tijera', 'QW8523', 1, 128, 'Pedro Faria', 1456, '12/06/2020'),
    (9251, 'piñón', 'EN5698', 2, 8, 'Juan Peña', 565, '12/06/2020'),
    (5489, 'tornillo', 'RS8512', 2, 33, 'Julio Perez', 3654213, '13/06/2020'),
    (3215, 'zocalo', 'UM8587', 2, 125, 'Laura Macias', 1256321, '13/06/2020'),
    (3698, 'biela', 'PT3218', 1, 78, 'Luis Peña', 14565487, '13/06/2020'),
    (8795, 'cilindro', 'AZ8794', 2, 96, 'Carlos Casio', 5612405, '13/06/2020'),
    (9852, 'Culata', 'XC9875', 2, 165, 'Luis Molero', 3455846, '14/06/2020'),
    (9852, 'Culata', 'XC9875', 2, 165, 'Jose Mejia', 1355846, '14/06/2020'),
    (2564, 'Cárter', 'PT29872', 2, 32, 'Peter Cerezo', 8545436, '14/06/2020'),
    (5412, 'válvula', 'AZ8798', 2, 11, 'Juan Peña', 568975, '14/06/2020')]  # lista de tuplas

idProducto = 9852  # idProducto

# imprime la funcion consultaRegistro
print(consultaRegistro(AutoPartes(ventas), idProducto))
