def Get_name():
    name = input("Name: ")
    return name

def get_tshirt():

    brands=["prada","LV","being HUman","zudio","balanciaga"]
    user=Get_name()
    brand_name= input("T-shirt brand you are looking for: ")
    if brand_name in brands:
     print(f"hi {user},Unfortunately the brand you are looking for is available.")
    else:
     print(f"hi {user},unfortunately the brand you are looking for is un available.")
get_tshirt()