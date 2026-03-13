# CICLO PARA VALIDAR PRECIO
while True:
        try:
            precio = int(input("Ingrese el precio del producto: "))
            
            if precio <= 0:
                print("Error: el precio debe ser mayor que 0")
            else:
                break
        
        except ValueError:
            print("Error: ingrese un valor numérico válido para el precio") 
            