"""
VIRTUAL STORE SYSTEM - CODE SUMMARY
================================================================================

MAIN.PY - Virtual Store Application
Allows users to add multiple products and view purchase history.

PRODUCTO.PY - Price Validation Utility
Validates that users enter positive numeric prices.

================================================================================
""" 
# MAIN APPLICATION FLOW
print("Welcome to the virtual store")  # Display welcome message
history = {}  # Dictionary to store: {product: {price, quantity, total}}
question = input("To start registering a new sale, type 'yes': ").strip().lower()

# Main shopping loop - repeats while user enters "yes"
while question in ("yes",):
    total_value = 0
    try:
        product = input("Enter the product name: ")
        
        # Validate price (must be positive integer)
        while True:
            try:
                price = int(input("Enter the product price: "))
                if price <= 0:
                    print("Error: price must be greater than 0")
                else:
                    break
            except ValueError:
                print("Error: you must enter a valid numeric value for the price")
        
        # Validate quantity (must be positive integer)
        while True:
            try:
                quantity = int(input("Enter the product quantity: "))
                if quantity <= 0:
                    print("Error: quantity must be greater than 0")
                else:
                    break
            except ValueError:
                print("Error: you must enter a valid numeric value for the quantity")
        
        # Calculate and store product details
        total = price * quantity
        history[product] = {"price": price, "quantity": quantity, "total": total}
        total_value += total
        
        # Ask to continue shopping
        question = input("Do you want to buy another product? (yes/no): ").lower()
        if question == "no" or question == "nope":
            print(f"The total to pay for {quantity} {product} is: {total} and the total value of your purchase is: {total_value}")
            print("Thank you for your purchase, see you soon")
            break
    
    except ValueError:
        print("Error: Please enter a valid numeric value for the price and quantity. Product not registered.")

# Display purchase history
print("End of program")
print("Purchase history:")
total_general = 0
for product, details in history.items():
    total_general += details["total"]
    print(f"Product: {product}, Price: {details['price']}, Quantity: {details['quantity']}")
print(f"Total purchase amount: {total_general}")

# KEY CONCEPTS:
# - Dictionary: stores product data as key-value pairs
# - try-except: catches invalid numeric input (ValueError)
# - while loops: validate input until conditions are met
# - f-strings: format output with variables
# - .strip().lower(): clean and normalize user input
# - += operator: accumulate totals

