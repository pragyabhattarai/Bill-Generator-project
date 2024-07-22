from datetime import datetime

def sales(operations):
    with open(str(operations.name) + str(operations.phone_number) + str(operations.address) + ".txt", "w") as file:
        file.write("\n")
        file.write("\n")
        file.write("--------------------------------------------------------------------------------------------------------------------------\n")
        file.write("                                                 Sunsine Laptop Shop                                                      \n")
        file.write("                                                         Bill                                                             \n")
        file.write("                                 Kaushaltar-01,Bhaktapur | Contact No:044-550324,9877068306                               \n")
        file.write("--------------------------------------------------------------------------------------------------------------------------\n")
        file.write("Customer Name: " + str(operations.name) + "\n")
        file.write("Phone Number: " + str(operations.phone_number) + "\n")
        file.write("Address: " + str(operations.address) + "\n")
        file.write("Date and time: " + str(datetime.now()) + "\n")
        file.write("--------------------------------------------------------------------------------------------------------------------------\n")
        file.write("ID \tLaptop Name \tBrand Name \tPrice \tQuantity \tAmount\n")
        file.write("--------------------------------------------------------------------------------------------------------------------------\n")
        for values in operations.Laptop_DC.values():
            file.write(str(values[0]) + "," + str(values[1]) + "," + str(values[2]) + "," + str(values[3]) + "," + str(values[4]) + "," + str(values[5]) + "\n")
        file.write("Total Amount: " + str(operations.total_amount) + "\n")
        file.write("Shipping Cost: " + str(operations.shipping_cost) + "\n")
        file.write("Final Amount: " + str(operations.final_amount) + "\n")
        file.write("--------------------------------------------------------------------------------------------------------------------------\n")
