def read_file():
    file = open("laptops.txt", "r")
    Laptop_DC = {}
    Laptop_ID = 1
    for line in file:
        line = line.replace("\n","")
        Laptop_DC.update({Laptop_ID: line.split(",")})
        Laptop_ID = Laptop_ID + 1
    file.close()
    return Laptop_DC
