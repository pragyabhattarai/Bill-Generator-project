import read
import write
import datetime
def welcome():
    print("--------------------------------------------------------------------------------------------------------------------------")
    print("                                                     Sunsine Laptop Shop                                                  ")
    print("                                                   Kaushaltar-01,Bhaktapur                                                ")
    print("                                             Contact no:044-550324,9877068306                                             ")
    print("                                               Email:Laptopshop72@email.com                                               ")
    print("--------------------------------------------------------------------------------------------------------------------------")
    print("                                                 Welcome to a Laptop Shop!                                                ")
    print("--------------------------------------------------------------------------------------------------------------------------")
    print("\n")


Laptop_DC = read.read_file()
def options():
    print("Press 1 to Sale from Shop.")
    print("Press 2 to Purchase from Shop.")
    print("Press 3 to Exit")
    print("\n")

def option_confirm():
    try:
        option = int(input("Enter your option: "))
    except ValueError:
        print("Please enter a valid option.")
        return option_confirm()
    while option:
        if option == 1:
            return sales()
        elif option == 2:
            return purchase()
        elif option == 3:
            return exit()
            
        else:
            print("Please enter the valid option")
            option = int(input("Enter your option: "))
       
def display_products():
    print("These are our available product Lists.")
    print("------------------------------------------------------------------------------------------------------------------------------------")
    print("ID \tLaptop Name \tBrand Name \tPrice \tQuantity Available \tProcessor Details \tGraphic Card Details")
    print("------------------------------------------------------------------------------------------------------------------------------------")

    file = open("laptops.txt", "r")
    ID = 1
    for line in file:
        print(ID, "\t\t"+line.replace(",", "\t\t"))
        ID = ID + 1
    print("------------------------------------------------------------------------------------------------------------------------------------")
    file.close()
    print("\n")


def get_product():
    while True:
        try:
            Product_ID = int(input("Enter the product ID: "))
        except ValueError:
            print("Please enter a valid laptop ID.")
            continue
        if 0 < Product_ID <= len(Laptop_DC):
            return Product_ID
        else:
            print("Please provide a valid Laptop ID!!")

def get_quantity(Product_ID):
    while True:
        try:
            Quantity = int(input("Enter the quantity: "))
        except ValueError:
            print("Please enter a valid quantity")
            continue
        selected_quantity = Laptop_DC[Product_ID][3]
        if 0 < Quantity <= int(selected_quantity):
            return Quantity
        else:
            print("Please provide a valid quantity!!")


def update_inventory(Product_ID, Quantity):
    Laptop_DC[Product_ID][3]= int(Laptop_DC[Product_ID][3])-int(Quantity)
    file = open("laptops.txt", "w")
    for values in Laptop_DC .values():
        file.write(str(values[0])+","+str(values[1])+","+str(values[2])+","+str(values[3])+","+str(values[4])+","+str(values[5]))
        file.write("\n")
        file.close()

#sales = write.sales()
def sales():
    print("--------------------------------------------------------------------------------------------------------------------------")
    print("To generate a bill, provide the customer details")
    print("--------------------------------------------------------------------------------------------------------------------------")
    name = input("Enter the name of the customer: ")
    phone_number = input("Enter the phone number of the customer: ")
    address = input("Enter the address of the customer: ")
    print("------------------------------------------------------------------------------------------------------------------------------------")
    print("\n")

    sold_laptops = {}  # create new dictionary to keep track of sold laptops
    total_amount = 0
    sale = True
    while sale:
        display_products()
        product_id = get_product()
        quantity = get_quantity(product_id)
        update_inventory(product_id, quantity)
        # update sold_laptops with the sold laptop
        if product_id in sold_laptops:
            sold_laptops[product_id]["Quantity"] += quantity  # add to existing quantity
        else:
            sold_laptops[product_id] = {
                "ID": product_id,
                "Laptop Name": Laptop_DC[product_id][0],
                "Brand Name": Laptop_DC[product_id][1],
                "Price": Laptop_DC[product_id][2],
                "Quantity": quantity
            }
        total_amount = float(Laptop_DC[product_id][2]) * quantity

        resale = input("Do you want to shop again? Type 'Yes' or 'No': ")
        while resale.lower() not in ["yes", "no"]:
            print("Please type 'Yes' or 'No' only!!")
            resale = input("Do you want to shop again? Type 'Yes' or 'No': ")

        if resale.lower() == "yes":
            print("You continue shopping.")
        else:
            print("\n")
            print("--------------------------------------------------------------------------------------------------------------------------")
            print("                                                 Sunshine Laptop Shop                                                      ")
            print("                                                         Bill                                                             ")
            print("                                 Kaushaltar-01, Bhaktapur | Contact No: 044-550324, 9877068306                              ")
            print("--------------------------------------------------------------------------------------------------------------------------")
            print("Customer Name: ", name)
            print("Phone Number: ", phone_number)
            print("Address: ", address)
            print("Date and time: ", datetime.datetime.now())
            print("--------------------------------------------------------------------------------------------------------------------------")
            print("ID \tLaptop Name \tBrand Name \tPrice \tQuantity \tAmount")
            print("--------------------------------------------------------------------------------------------------------------------------")
            for laptop in sold_laptops.values():
                amount = float(laptop["Price"]) * laptop["Quantity"]
                print(laptop["ID"], "\t", laptop["Laptop Name"], "\t", laptop["Brand Name"], "\t", laptop["Price"], "\t", laptop["Quantity"], "\t", amount)
            print("--------------------------------------------------------------------------------------------------------------------------")
            shipping_cost = 100
            final_amount = total_amount + shipping_cost
            print("Total Amount: ", total_amount)
            print("Shipping Cost: ", shipping_cost)
            print("Final Amount: ", final_amount)
            print("--------------------------------------------------------------------------------------------------------------------------")
            break

def purchase():
    print("purchase")

def display_products():
    print("These are our available product Lists.")
    print("------------------------------------------------------------------------------------------------------------------------------------")
    print("ID \t\tLaptop Name           Brand Name        \tPrice \tQuantity Available \tProcessor Details \tGraphic Card Details")
    print("------------------------------------------------------------------------------------------------------------------------------------")

    file = open("laptops.txt", "r")
    ID = 1
    for line in file:
        print(ID, "\t\t"+line.replace(",", "\t\t"))
        ID = ID + 1
    print("------------------------------------------------------------------------------------------------------------------------------------")




##############3

def get_product1():
    while True:
        try:
            Product_ID1 = int(input("Enter the product ID: "))
        except ValueError:
            print("Please enter a valid laptop ID.")
            continue
        if 0 < Product_ID1 <= len(Laptop_DC):
            return Product_ID1
        else:
            print("Please provide a valid Laptop ID!!")

def get_quantity1(Product_ID1):
    while True:
        try:
            Quantity1 = int(input("Enter the quantity: "))
        except ValueError:
            print("Please enter a valid quantity")
            continue
        selected_quantity = Laptop_DC[Product_ID1][3]
        if 0 < Quantity1 <= int(selected_quantity):
            return Quantity1
        else:
            print("Please provide a valid quantity!!")


def update_inventory1(Product_ID1, Quantity1):
    Laptop_DC[Product_ID1][3]= int(Laptop_DC[Product_ID1][3])+int(Quantity1)
    file = open("laptops.txt", "w")
    for values in Laptop_DC .values():
        file.write(str(values[0])+","+str(values[1])+","+str(values[2])+","+str(values[3])+","+str(values[4])+","+str(values[5]))
        file.write("\n")
    file.close()


def purchase():
    print("--------------------------------------------------------------------------------------------------------------------------")
    print("To generate a bill, provide the shop details")
    print("--------------------------------------------------------------------------------------------------------------------------")
    name = input("Enter the name of the shop: ")
    phone_number = input("Enter the fax number of the shop: ")
    Address = input("Enter the address of the shop: ")
    print("------------------------------------------------------------------------------------------------------------------------------------")
    print("\n")

    purchase_dc = {}  # create new dictionary to keep track of sold laptops
    total_amount = 0
    purchase = True
    while purchase:
        display_products()
        Product_ID1 = get_product1()
        Quantity1 = get_quantity1(Product_ID1)
        update_inventory1(Product_ID1, Quantity1)
        # update sold_laptops with the sold laptop
        if Product_ID1 in purchase_dc:
            purchase_dc[Product_ID1]["Quantity"] += Quantity1  # add to existing quantity
        else:
            purchase_dc[Product_ID1] = {
                "ID": Product_ID1,
                "Laptop Name": Laptop_DC[Product_ID1][0],
                "Brand Name": Laptop_DC[Product_ID1][1],
                "Price": Laptop_DC[Product_ID1][2],
                "Quantity": Quantity1
            }
        total_amount += float(Laptop_DC[Product_ID1][2]) * Quantity1

        resale = input("Do you want to purchase again? Type 'Yes' or 'No': ")
        while resale.lower() not in ["yes", "no"]:
            print("Please type 'Yes' or 'No' only!!")
            resale = input("Do you want to purchase again? Type 'Yes' or 'No': ")

        if resale.lower() == "yes":
            print("You continue shopping.")
        else:
            print("\n")
            print("--------------------------------------------------------------------------------------------------------------------------")
            print("                                                 Rising Star Laptop Shop                                                      ")
            print("                                                         Bill                                                             ")
            print("                                 Thimi-01,Bhaktapur | Contact No:044-550324,9877068306                               ")
            print("--------------------------------------------------------------------------------------------------------------------------")
            print("Customer Name: ", name)
            print("Phone Number: ", phone_number)
            print("Address: ", Address)
            print("Date and Time: ", datetime.now())
            print("--------------------------------------------------------------------------------------------------------------------------")
            print("ID \tLaptop Name \tBrand Name \tPrice \tQuantity \tAmount")
            print("--------------------------------------------------------------------------------------------------------------------------")
            for laptop in purchase_dc.values():
                amount = float(laptop["Price"]) * laptop["Quantity"]
                print(laptop["ID"], "\t", laptop["Laptop Name"], "\t", laptop["Brand Name"], "\t", laptop["Price"], "\t", laptop["Quantity"], "\t", amount)
            print("--------------------------------------------------------------------------------------------------------------------------")
            Vat_rate = 0.13
            Vat_amount = total_amount * Vat_rate
            final_amount = total_amount + Vat_amount
            print("Total Amount: ", total_amount)
            print("Vat amount: ", Vat_amount)
            print("Final Amount with Vat: ", final_amount)
            print("--------------------------------------------------------------------------------------------------------------------------")
            break
def exit():
        print("You have successfully exited the system")
    