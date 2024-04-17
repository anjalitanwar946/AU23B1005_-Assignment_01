def get_order():
    orders=["momos","maggi","pasta"]
    order=0
    for order in reversed(orders):
        print(f"preparing your {order}")
      
    print("Following order has been Dispatvhed")

    while orders:
        print(orders.pop())

get_order()