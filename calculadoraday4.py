# permite ingresar al usuario, se pone int para convertir el imput 
# exclusivamente en un numero entero
numero = int(input("ingresar un numero: "))


numero2 = int(input("ingresar otro numero: "))

# se usa print para mostrar el resultado, se utilizan las variables
# por que guardan los valores guardados en la variable anterior 
# y se les asigna en el print varias operaciones correspondientes con sus signos
print ("la suma es", numero + numero2)
print ("la resta es", numero - numero2) 
print ("la multiplicacion es", numero * numero2)
# este print muestra el resultado de la division decimal
# el / muestra numeros decimales,
print ("la division decimal es", numero / numero2)
# este print muestra el resultado de la division entera
# esta // solo da resultados de numeros enteros, como un 4, sin puntos
# ni medios la entera se corta no se redondea
print ("la division entera es", numero // numero2)

