print("bienvenido a la tienda virtual") 
historial = {}
pregunta =  input("Para inciar el registro de una nueva venta, escriba 'si': ").strip().lower() #strip() elimina los espacios en blanco al inicio y al final de la cadena, lower() convierte la cadena a minúsculas para facilitar la comparación con "si" o "yes"
status = ("si", "yes") 
while pregunta in status : #while ciclo repetitivo, se ejecuta mientras la condición sea verdadera, en este caso, mientras la variable pregunta sea igual a "si" o "yes"    
    total_valor = 0
    try:      
       
       
        producto = input("ingrese el nombre del producto: ")
       
        
   # CICLO PARA VALIDAR PRECIO
        while True:
                try:
                    precio = int(input("Ingrese el precio del producto: "))

                    if precio <= 0:
                        print("Error: el precio debe ser mayor que 0")
                    else:
                        break

                except ValueError:
                    print("Error: debe ingresar un valor numérico válido para el precio")        
        
   # CICLO PARA VALIDAR CANTIDAD
        while True:
                try:
                    cantidad = int(input("Ingrese la cantidad del producto: "))

                    if cantidad <= 0:
                        print("Error: la cantidad debe ser mayor que 0")
                    else:
                        break

                except ValueError:
                    print("Error: debe ingresar un valor numérico válido para la cantidad")       
        total = precio * cantidad
       
        historial[producto] = {"precio": precio, "cantidad": cantidad, "total": total} 
       
        total_valor += historial[producto]["total"]
       
        pregunta = input("¿desea comprar otro producto? (si/no): ").lower()
        if pregunta == "no" or pregunta == "nope":
       
            print(f"el total a pagar por {cantidad} {producto} es: {total} and el valor total de su compra es: {total_valor}")
            print("gracias por su compra, vuelva pronto")
            break
    except ValueError:
        print("Error: Por favor, ingrese un valor numérico válido para el precio y la cantidad. Producto no registrado.")

print(("Fin del programa"))
print("Historial de compras:")
total_general = 0
for producto, detalles in historial.items():
    total_general+= detalles["total"]
    print(f"Producto: {producto}, Precio: {detalles['precio']}, Cantidad: {detalles['cantidad']}")  
print(f"Total general de la compra: {total_general}")



