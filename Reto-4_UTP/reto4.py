def ordenes(rutinaContable):
    print('------------------------ Inicio Registro diario ---------------------------------')

    from functools import reduce
    total = list(
        map(lambda x: [x[0]] + list(map(lambda y: y[1] * y[2], x[1:])), rutinaContable))
    total = list(
        map(lambda x: [x[0]] + [reduce(lambda a, b: round(a + b, 2), x[1:])], total))
    total = list(map(lambda x: x if x[1] >= 600000 else [
                 x[0], x[1] + 25000], total))
    for i in total:
        print(f'La factura {i[0]} tiene un total en pesos de {i[1]:,.2f}')
    print('-------------------------- Fin Registro diario ----------------------------------')


rutinaContable = [
    [6589, ("9874", 1, 125698.20), ("88112", 2,
                                    135645.20), ("3218", 4, 13645.20)],
    [6590, ("5236", 8, 11.99), ("7733", 11, 18.99), ("88112", 5, 390.95)],
    [6591, ("7812", 2, 11.99), ("9652", 11, 18.99)],
]

ordenes(rutinaContable)

# [
#     [6589, ("9874", 1, 125698.20), ("88112", 2,
#                                     135645.20), ("3218", 4, 13645.20)],
#     [6590, ("5236", 8, 11.99), ("7733", 11, 18.99), ("88112", 5, 390.95)],
#     [6591, ("7812", 2, 11.99), ("9652", 11, 18.99)], ]


# salida = ------------------------ Inicio Registro diario - --------------------------------
# La factura 1201 tiene un total en pesos de 962, 529.33
# La factura 1202 tiene un total en pesos de 413, 477.56
# La factura 1203 tiene un total en pesos de 443, 859.80
# La factura 1204 tiene un total en pesos de 27, 247.57
# -------------------------- Fin Registro diario - --------------------------------

# print('----------------- Inicio Registro diario --------------------------')
# print('------------------------ Inicio Registro diario ---------------------------------')

# print('----------------- Fin Registro diario -----------------------------')
# print('-------------------------- Fin Registro diario ----------------------------------')
