# Reto2 UTP

Reto 2:
En el parque de diversiones “AVENTURAS EXTREMAS” se requiere implementar una función en la cual reciba como parámetro un diccionario, el cual va a tener las variables que a continuación se muestran:

![image](https://user-images.githubusercontent.com/29380120/169149598-e002b44e-5965-49fb-bcad-98b66c997177.png)

En la siguiente tabla se muestra la atracción y el valor de la boleta para cada una de ellas, en la cual los clientes podrán ingresar dependiendo de su edad, posteriormente el parque de atracciones ha decidido otorgar un descuento al valor de la boleta si cumple con el rango de edad y es la primera vez que el cliente ingresa.

![image](https://user-images.githubusercontent.com/29380120/169149625-b38d1c03-bbb5-476c-a018-5819e9c8ca31.png)


Esta función debe retornar un nuevo diccionario con las llaves nombre, edad, atracción, primer_ingreso, total_boleta y apto del cliente:
• En donde apto tendrá como valor una variable booleana, será verdadera si su edad cumple con los rangos exigidos en la tabla anterior, en el caso contrario será falsa.
• En el caso de atraccion y total_boleta, si no se cumple el rango de edades se le asignara un valor de ‘N/A’ a cada uno.
• Si primer_ingreso es verdadero, el total_boleta será el valor de la boleta menos el descuento de lo contrario se pagará el valor neto de la boleta.

![image](https://user-images.githubusercontent.com/29380120/169149671-f7bff44d-ab88-4251-89d5-3718823496e6.png)


