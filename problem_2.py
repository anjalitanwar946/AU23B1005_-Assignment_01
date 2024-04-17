def Get_name():
    name = input("Name: ")
    return name

def get_tshirt():
    size=["s","m","l","xl"]
    brands=["Prada","LV","Being HUman","Zudio","Balanciaga"]
    user=Get_name()
    print("BRANDS\n","Prada\n", "LV\n", "Gucci\n", "Zudio\n", "Balanciaga")
    brand_name= input("T-shirt brand you are looking for: ")
    if brand_name in brands:
     user_size=input("Enter Size: ")
    
     if user_size in size: 
       print(f"Hi {user},the brand you are looking for is available in this size.")
     else:
       print(f"Hi {user},Unfortunately the brand you are looking for is un available in this size.")
    else:
     print(f"Hi {user},Unfortunately the brand you are looking for is un available.")
get_tshirt()
