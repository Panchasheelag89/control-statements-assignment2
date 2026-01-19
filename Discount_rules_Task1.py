order_input = input('enter your order amount:')
if not order_input.isdigit():
    print('Pleae enter valid number')
else:
    order_input = int(order_input)

    if order_input>=2000:
        discount = 15
    elif  1500<=order_input<2000:
        discount = 10
    elif 1000<=order_input<1500:
        discount = 7
    else:
        discount = 0


    final_amount = order_input - (order_input * discount / 100)
    print(f"Order amount: {order_input}")
    print(f"Discount: {discount}%")
    print(f"Final amount: {final_amount}")    

