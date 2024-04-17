def get_order():
    orders=["momos","maggi","pasta"]
    i=0
    for i in reversed(orders):
        print(f"preparing your {i}")
      
    print("Following order has been Dispatvhed")

    while orders:
        print(orders.pop())

get_order()