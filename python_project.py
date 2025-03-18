from prettytable import PrettyTable


def display_table(list_dict:list):
    """
    Displays a formatted table of products using the PrettyTable module.

    Parameters:
    list_dict (list of dict): A list of dictionaries, where each dictionary represents 
                              a product with the keys "Name", "Price", and "QTY".

    Returns:
    PrettyTable: A formatted table displaying the product details.
    
    Example:
    products = [
        {"Name": "Laptop", "Price": 1200, "QTY": 5},
        {"Name": "Mouse", "Price": 25, "QTY": 10}
    ]
    
    print(display_table(products))
    """ 

    #using PrettyTable module to display the products
    table = PrettyTable()
    #naming the table fields header
    table.field_names = ["Name", "Price", "QTY"]
    # Add rows to the table
    for product in list_dict:
        table.add_row([product["Name"], product["Price"], product["QTY"]])
    #displaying the products
    return table


#calculating the price with discount
#defining function for calculting the discount
def calculte_discount(qty:int):
    """
    Calculates the discount percentage based on the quantity purchased.

    Parameters:
    qty (int): The quantity of items purchased.

    Returns:
    float: The discount rate as a decimal (e.g., 0.05 for 5%).

    Discount tiers:
    - 250 to 499 items: 5% discount
    - 500 to 749 items: 10% discount
    - 750 to 999 items: 15% discount
    - 1000 to 1249 items: 20% discount
    - 1250 to 1499 items: 25% discount
    - Below 250 or above 1500: No discount (0%)

    Example:
    >>> calculate_discount(300)
    0.05
    >>> calculate_discount(800)
    0.15
    >>> calculate_discount(2000)
    0.0
    """
    if qty >= 250 and qty < 500:
        return 0.05 # discount 5%
    elif qty >= 500 and qty < 750:
        return 0.1 # discount 10%
    elif qty >= 750 and qty < 1000:
        return 0.15 # discount 15%
    elif qty >= 1000 and qty < 1250:
        return 0.2 # discount 20%
    elif qty >= 1250 and qty < 1500:
        return 0.25 # discount 25%
    else:
        return 0 # discount 0%


#defining the bill function
def bill(price_list:list,qty_list:list,discount:float):
    """
    Calculates and displays the total bill amount after applying a discount.

    Parameters:
    price_list (list of float): A list of product prices.
    qty_list (list of int): A list of quantities corresponding to the products.
    discount (float): The discount rate as a decimal (e.g., 0.1 for 10%).

    Returns:
    float: The total bill amount after applying the discount.

    Example:
    >>> bill([10.0, 20.0, 30.0], [2, 3, 1], 0.1)
    
    Output:
    the bill amount = $110.0
    You have discount = 10%
    the bill amount after discount = $99.0
    
    Returns:
    99.0
    """
    # calculating the items price  = Price x QTY for each product
    total_price = sum([i*j for i,j in zip(qty_list,price_list)])
    # calculating the price after the discount
    price_after_discount = total_price * (1-discount)

    #display the price
    print(f"\nthe bill amount = ${round(total_price,2)}")
    print(f"You have discount = {int(discount*100)}%")
    print(f"the bill amount after discount = ${round(price_after_discount,2)}\n")
    return price_after_discount


# creating th list of products
products = [
    {"Name": "Laptop",     "Price": 1200,  "QTY": 50},
    {"Name": "Smart Phone", "Price": 800,  "QTY": 75},
    {"Name": "Headphones", "Price": 150,   "QTY": 200},
    {"Name": "Keyboard",   "Price": 100,   "QTY": 500},
    {"Name": "Mouse",      "Price": 50,    "QTY": 500},
    {"Name": "Monitor",    "Price": 300,   "QTY": 50},
    {"Name": "Usb Drive",  "Price": 20,    "QTY": 500},
    {"Name": "Hard Drive", "Price": 120,   "QTY": 200},
]

#creating empty lists to handle the purchased products name, price, and quantity        
name_list = list(); price_list = list(); qty_list = list()


#difine function to validate product name and quantity
def valid_product_name_qty(name:str,product,disc_fucn,bill_func):
    """
    Validates a product name and its quantity, updates stock, and calculates the bill.

    Parameters:
    name (str): The name of the product selected by the user.
    product (list of dict): A list of available products, each represented as a dictionary 
                            with keys "Name", "Price", and "QTY".
    disc_func (function): A function that calculates the discount based on the total quantity.
    bill_func (function): A function that calculates and displays the final bill.

    Returns:
    tuple or None: Returns a tuple (product_name, price, quantity) if a valid selection is made;
                   otherwise, returns None.

    Behavior:
    - The function continuously prompts the user for a valid product name.
    - If 'Q' is entered, the function exits.
    - It validates the product name and checks for stock availability.
    - If a valid quantity is entered, it updates the stock and processes the bill.
    - If an invalid product or quantity is entered, it prompts the user again.

    Example Usage:
    >>> products = [{"Name": "Laptop", "Price": 1000, "QTY": 5}]
    >>> valid_product_name_qty("Laptop", products, calculate_discount, bill)
    
    """
  
    while True:
        if name == 'Q': #Quiting the loop 

            break
        else: # validating the product and its quantity
            for i in product: 
                if name == i['Name'] : #validating the product name
                    print(f"\nYou Chose => [ {name} ]\n") #display the chosen product
                    #extracting the product price
                    price = i["Price"]
                    #asking the user to input the product required quantity
                    qty = input("Please Enter the Required Quantity = ")
                    while True: 
                        try: # to handle the ValueError of quantity
                            qty_int = int(qty)
                            if i["QTY"] >= qty_int and qty_int >0: # validating the product quantity
                                #display the product name and its quantity
                                print(f"\nYou Chose => [ {name} ], With Quantity => [ {qty_int} ]\n ")
                                # deduct the purchased quantity from the available quantity
                                i["QTY"] -=  qty_int
                                #fill the name, price, quantity lists
                                name_list.append(name)
                                price_list.append(price)
                                qty_list.append(qty_int)
                                #calcultaing final bill with discount
                                discount = disc_fucn(sum(qty_list))
                                bill_func(price_list,qty_list,discount)
                                #output the purchased product name, price and quantity
                                return name,price,qty_int 
                                break
                            
                            else: # informing the user to input valid product quantity
                                print(f"\n⚠️  The available Quantity for [{name}] => {i["QTY"]} ⚠️ \n")
                                qty = input("Enter the Required Quantity:  ")
                        except ValueError : # informing the user to input correct product quantity data type
                            print(f"\n⚠️  Please Enter Number ⚠️ \n")
                            qty = input("Enter the Required Quantity:  ")
                  
            # informing the user to input valid product    
            print("\n⚠️  You entered invalid product ⚠️ \n")
            print("The available products are: ")
            prod_table = display_table(product)
            print(prod_table)
            name = input("Choose product, or press 'q' to quit  \n").strip().title()



#def prompt function to take products name and quantity from the user
def prompt(prod, disc_fucn ,bill_func):
    """
    Prompts the user to select products, validates input, and processes billing.

    Parameters:
    prod (list of dict): A list of available products, each represented as a dictionary 
                         with keys "Name", "Price", and "QTY".
    disc_func (function): A function that calculates the discount based on the total quantity.
    bill_func (function): A function that calculates and displays the final bill.

    Returns:
    None

    Behavior:
    - Displays the available products.
    - Prompts the user to choose a product or quit by entering 'Q'.
    - Calls `valid_product_name_qty()` to validate and process the selection.
    - If `valid_product_name_qty()` returns `None`, the loop breaks, stopping further prompts.

    Example Usage:
    >>> prompt(products, calculate_discount, bill)
    """
 
    while True:
        #prompt the user to enter the product name
        prod_table = display_table(prod)
        print(prod_table)
        name  = input("Choose product, or press 'q' to quit  \n").strip().title()
        if name == 'Q': # check to quit the loop
            break
        else:
            func_out = valid_product_name_qty(name,prod,disc_fucn,bill_func)
            if not func_out: # check is valid_product_name_qty() function is empty
                break

#calling the prompt function 
print("Hello!, The available products are: ")
prompt(products,calculte_discount,bill)
#calcultaing final bill with discount
discount = calculte_discount(sum(qty_list))
#Displaying the final product bill
print("\nYour Bill:")
final_product_price = bill(price_list,qty_list,discount)

        

#calculating the price with discount for stationary products
#defining function for calculting the discount
def calculte_discount_st(qty:int):
    """
    Calculates a stepwise discount based on the quantity purchased.

    Parameters:
    qty (int): The quantity of items purchased.

    Returns:
    float: The discount rate as a decimal (e.g., 0.02 for 2%).

    Discount Calculation:
    - A discount of 2% (0.02) is applied for every 50 units purchased.
    - Example:
      - 50 units → 2% discount (0.02)
      - 100 units → 4% discount (0.04)
      - 150 units → 6% discount (0.06), and so on.
    - If qty is less than 50, no discount is applied.

    Example Usage:
    >>> calculate_discount_st(120)
    0.04

    >>> calculate_discount_st(75)
    0.02

    >>> calculate_discount_st(30)
    0.0
    """
    return (qty//50)*0.02

#creating empty lists to handle the purchased products name, price, and quantity        
name_list = list(); price_list = list(); qty_list = list() 
# Stationary Stor Functionality
def stationary_store():
    """
    Simulates a stationary store where users can select and purchase products.

    Returns:
    float: The total bill amount after applying any discounts.

    Behavior:
    - Initializes a list of stationary products, each with a name, price, and available quantity.
    - Displays the available products using `display_table()`.
    - Calls the `prompt()` function to allow the user to select products and quantities.
    - Calculates the total discount using `calculate_discount_st()`.
    - Displays and calculates the final bill using `bill()`.
    - Returns the total amount after applying the discount.

    Example Usage:
    >>> final_price = stationary_store()
    Hello! The available stationary products are:
    (Displays product table)
    (User selects products)
    Your Bill:
    (Displays final bill)
    
    Returns:
    - The final amount after applying the discount.
    """
    
    # creating th list of products
    stationary_products = [
                            {"Name": "Notebook",   "Price": 2.5, "QTY": 100},
                            {"Name": "Pen",        "Price": 0.8, "QTY": 200},
                            {"Name": "Pencil",     "Price": 0.5, "QTY": 300},
                            {"Name": "Eraser",     "Price": 0.3, "QTY": 150},
                            {"Name": "Ruler",      "Price": 1.2, "QTY": 100},
                            {"Name": "Sharpener",  "Price": 0.7, "QTY": 150},
                            {"Name": "Marker",     "Price": 1.5, "QTY": 150},
                            {"Name": "Glue Stick", "Price": 1.0, "QTY": 100},
                            {"Name": "Scissors",   "Price": 3.0, "QTY": 50},
                            {"Name": "Stapler",    "Price": 4.5, "QTY": 200}
                           ]
    
    tabl = display_table(stationary_products)
    #calling the prompt function 
    print("Hello!, The available Stationary products are: ")
    prompt(stationary_products,calculte_discount_st,bill)
    #calcultaing final bill with discount
    discount = calculte_discount(sum(qty_list))
    #Displaying the final product bill
    print("\nYour Bill:")
    final_product_price = bill(price_list,qty_list,discount)
    return final_product_price

final_product_st_price = stationary_store()
#calulating the final price for products and stationary products
final_price = final_product_price + final_product_st_price
#dispalying the final price
print(f"\nThe total Bill Amount of [devices & Stationary] Products after the Dsicount  = ${final_price}\n")

#definig function to ask the user to choose between "delivery" or "pick-up"
#and calculating the price after the choice   
def delivery_or_pickup(price):
    """
    Determines whether the customer wants delivery or pick-up and adjusts the bill accordingly.

    Parameters:
    price (float): The total bill amount before adding delivery or pick-up charges.

    Returns:
    float: The final bill amount after adding the selected delivery or pick-up charge.

    Behavior:
    - Prompts the user to choose between:
      - Delivery (`D`): Adds a $200 charge.
      - Pick-up (`P`): Adds a $50 charge.
      - Any other input keeps the bill unchanged.
    - Displays the updated bill amount after applying the selected option.

    Example Usage:
    >>> delivery_or_pickup(500)
    press 'D' for Delivery, or press 'P' for Pick-Up: D
    You Chose Delivery Option, so $200 will be added to your bill.
    The Bill Amount after Discount and Delivery = $700.0

    >>> delivery_or_pickup(300)
    press 'D' for Delivery, or press 'P' for Pick-Up: P
    You Chose Pick-Up Option, so $50 will be added to your bill.
    The Bill Amount after Discount and Pick-Up = $350.0

    >>> delivery_or_pickup(250)
    press 'D' for Delivery, or press 'P' for Pick-Up: X
    You Did not Choose either Delivery or Pick-Up.
    The Bill Amount after Discount = $250.0
    """
    choice = input("press 'D' for Delivery, or press 'P' for Pick-Up: ").strip().capitalize()
    if choice == "D":
        final_price_after_delivery_pickup = price + 200
        print("\nYou Chose Delivey Option, so $200 will be add to your bill")
        print(f"The Bill Amount after Discount and Delivery = ${final_price_after_delivery_pickup}\n")
        return final_price_after_delivery_pickup
    elif choice == "P":
        final_price_after_delivery_pickup = price + 50
        print("\nYou Chose Pick-UP Option, so $50 will be add to your bill")
        print(f"The Bill Amount after Dicount and Pick-Up = ${final_price_after_delivery_pickup}\n")
        return final_price_after_delivery_pickup
    else:
        print("\nYou Did not Choose either to Delivery or Pick-up")
        print(f"The Bill Amount after Discount = ${price}\n")
        return price
    
#calulating price after Delivery of pick-up for products and stationary products
final_price_after_delivery_pickup = delivery_or_pickup(final_price)

#currency conversion function
def currency_conversion(price):
    """
    Converts the total bill amount into a selected currency (USD, EUR, or EGP).

    Parameters:
    price (float): The total bill amount in USD before conversion.

    Returns:
    float: The converted price in the chosen currency.

    Behavior:
    - Prompts the user to choose a currency from ["USD", "EUR", "EGP"].
    - Converts the price based on the following exchange rates:
      - EUR: 1 USD = 0.92 EUR
      - EGP: 1 USD = 30 EGP
      - Default currency is USD (no conversion).
    - Displays the final bill amount in the selected currency.
    - Returns the converted price.

    Example Usage:
    >>> currency_conversion(100)
    Choose currency from ["USD", "EUR", "EGP"]: EUR
    The Total Bill Amount in EUR = 92.00
    Your order is on the way

    >>> currency_conversion(100)
    Choose currency from ["USD", "EUR", "EGP"]: EGP
    The Total Bill Amount in EGP = 3,000.00
    Your order is on the way

    >>> currency_conversion(100)
    Choose currency from ["USD", "EUR", "EGP"]: USD
    The Total Bill Amount in USD = 100.00
    Your order is on the way
    """
    currency = input('Choose currency from ["USD", "EUR", "EGP"]: ').upper()
    if currency == "EUR":
        p = price * 0.92
        print(f"\nThe Total Bill Amount in EUR = {p:,.2f}\nYour order is on the way")

        return p
    elif currency == "EGP":
        p = price * 30
        print(f"\nThe Total Bill Amount in EGP = {p:,.2f}\nYour order is on the way")
        return p
    else:
        print(f"\nThe Total Bill Amount in USD = {price:,.2f}\nYour order is on the way")
        return price
    
#calcutating price after currency conversion
price_after_currency_conversion = currency_conversion(final_price_after_delivery_pickup)










