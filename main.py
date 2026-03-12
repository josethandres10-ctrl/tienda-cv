print("Welcome to the virtual store") 
history = {}
question =  input("To start registering a new sale, type 'yes': ").strip().lower() # strip() removes whitespace at the beginning and end of the string, lower() converts the string to lowercase for easier comparison with "yes"
status = ("yes",) 
while question in status : # while loop, executes as long as the condition is true, in this case, while the question variable is equal to "yes"    
    total_value = 0
    try:      
       
       
        product = input("Enter the product name: ")
       
        
   # LOOP TO VALIDATE PRICE
        while True:
                try:
                    price = int(input("Enter the product price: "))

                    if price <= 0:
                        print("Error: price must be greater than 0")
                    else:
                        break

                except ValueError:
                    print("Error: you must enter a valid numeric value for the price")        
        
   # LOOP TO VALIDATE QUANTITY
        while True:
                try:
                    quantity = int(input("Enter the product quantity: "))

                    if quantity <= 0:
                        print("Error: quantity must be greater than 0")
                    else:
                        break

                except ValueError:
                    print("Error: you must enter a valid numeric value for the quantity")       
        total = price * quantity
       
        history[product] = {"price": price, "quantity": quantity, "total": total} 
       
        total_value += history[product]["total"]
       
        question = input("Do you want to buy another product? (yes/no): ").lower()
        if question == "no" or question == "nope":
       
            print(f"The total to pay for {quantity} {product} is: {total} and the total value of your purchase is: {total_value}")
            print("Thank you for your purchase, see you soon")
            break
    except ValueError:
        print("Error: Please enter a valid numeric value for the price and quantity. Product not registered.")

print("End of program")
print("Purchase history:")
total_general = 0
for product, details in history.items():
    total_general+= details["total"]
    print(f"Product: {product}, Price: {details['price']}, Quantity: {details['quantity']}")  
print(f"Total purchase amount: {total_general}")



