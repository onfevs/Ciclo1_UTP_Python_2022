# Reto 1 UTP (MinTic)
## Ciclo 1 Fundamentos de programacion Reto 1

Descripción del problema: Una entidad Bancaria o entidad financiera, requiere calcular el valor de los intereses ganados y el total final de dinero para diferentes clientes, de acuerdo, a una cantidad de dinero invertida en un CDT. Un CDT por su parte, es un producto financiero que ofrece la posibilidad de guardar dinero durante un tiempo determinado para recibir posteriormente sus intereses devengados, asimismo, ofrece rendimientos a una tasa fija, asegurando una rentabilidad libre de riesgo en un tiempo determinado que por lo general debe ser mayor a dos (2) meses. Si, este dinero se retira antes de este periodo se aplica una penalidad del 2%. En ese sentido, el valor de los intereses ganados por un periodo de tiempo superior a dos meses se determina a través de la siguiente formula:

![image](https://user-images.githubusercontent.com/29380120/168408086-7fc34940-e023-4aac-ab94-f2f3a3c59789.png)

Donde:
cantidad = dinero ingresado en el CDT
porcentaje_interes = 3% (0.03).
tiempo = cantidad de tiempo
En consecuencia, el valor total del dinero será calculado a través de la siguiente formula:

![image](https://user-images.githubusercontent.com/29380120/168408097-3ec48015-88be-48d9-bbd6-1f0b266f0bf4.png)

Se debe determinar el valor total a retirar por el cliente que invirtió en el CDT al final del periodo.
Por otra parte, para un periodo de tiempo inferior o igual a dos meses se debe aplicar la siguiente formula:

![image](https://user-images.githubusercontent.com/29380120/168408105-8eee598d-f85b-433d-8ca1-298ccd0beea7.png)

Donde:
cantidad = dinero ingresado en el CDT
procentajea perder = 2% (0.02)
En consecuencia, el valor total del dinero será calculado a través de la siguiente formula:

![image](https://user-images.githubusercontent.com/29380120/168408119-87a9e9da-3b70-41dd-9c26-c10c8763a783.png)

Para responder a este planteamiento, escriba una función que reciba como parámetros: una cadena con el usuario del cliente como dato alfanumérico, el capital aportado y el tiempo del CDT y, en consecuencia, retorne una cadena de caracteres que le proporcione al banco la información que desea obtener.
La cadena debe tener para el caso de las ganancias, la siguiente estructura:
“Para el usuario {} La cantidad de dinero a recibir, según el monto inicial {} para un tiempo de {} meses es: {}”
para el caso de las pérdidas:
“Para el usuario {} La cantidad de dinero a recibir, según el monto inicial {} para un tiempo de {} meses es: {}”

![image](https://user-images.githubusercontent.com/29380120/168408141-5783a0d6-aaca-43ac-aee9-6e0d2faa896c.png)
