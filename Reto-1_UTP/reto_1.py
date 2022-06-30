
"""
cantidad = "dinero ingresado en el CDT"
porcentajeInteres = 3 % (0.03)
porcentajePerder = 2 % (0.02)
tiempo = "cantidad de tiempo"

valorTotal = valorInteres + cantidad

valorTotalPerder = cantidad - valorPerder

valorPerder = cantidad * porcentajePerder

valorInteres = cantidad * porcentajeInteres * tiempo / 12

# Para el caso de las ganancias

“Para  el  usuario  {}  La  cantidad  de  dinero  a  recibir,  según  el  monto  inicial  {}  para  un
tiempo de {} meses es: {}”

# Para el caso de perdidas

“Para  el  usuario  {}  La  cantidad  de  dinero  a  recibir,  según  el  monto  inicial  {}  para  un
tiempo de {} meses es: {}” """


def CDT(usuario: str, capital: int, tiempo: int):

    if tiempo <= 2:
        porcentajePerder = 2
        valorPerder = capital * (porcentajePerder/100)
        valorTotal = capital - valorPerder
        return (f"Para el usuario {usuario} La cantidad de dinero a recibir, según el monto inicial {capital} para un tiempo de {tiempo} meses es: {valorTotal}")

    else:
        porcentajeInteres = 3
        valorInteres = capital * (porcentajeInteres/100) * tiempo / 12
        valorTotal = capital + valorInteres
        return f"Para el usuario {usuario} La cantidad de dinero a recibir, según el monto inicial {capital} para un tiempo de {tiempo} meses es: {valorTotal}"


print('----------------------------------------')
print(CDT("ER3366", 650000, 2))  # Para el caso de < 2 meses
print(CDT("ER3366", 50000, 1))
print(CDT("AB1012", 1000000, 3))  # Para el caso de > 2 meses
print(CDT("AB1012", 10000000, 12))

# print(f"Para el usuario {usuario} La cantidad de dinero a recibir, según el monto inicial {capital} para un tiempo de {tiempo} meses es: {valorTotal}")
# print("Para el usuario" + usuario + " La cantidad de dinero a recibir, según el monto inicial " + capital + " para un tiempo de " + tiempo + " meses es: " + valorTotal")
# print("Para el", usuario, "La cantidad de dinero a recibir, según el monto inicial", capital, "para un tiempo de", tiempo, "meses es: ", valorTotal")
# print("Para el % s La cantidad de dinero a recibir, según el monto inicial % s para un tiempo de % s meses es: %s" %(usuario, capital, tiempo, valorTotal))
#print("Para el usuario {} la cantidad de dinero a recibir, según el monto inicial {} para un tiempo de {} meses es: {}".format(usuario, capital, tiempo, valorTotal))
