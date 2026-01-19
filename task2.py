orders = [1200, 2500, 800, 1750, 3000]

total_revenue = 0
for order_amount in orders:
    if order_amount >= 2000:
        discount = 15
    elif 1500 <= order_amount < 2000:
        discount = 10
    elif 1000 <= order_amount < 1500:
        discount = 7
    else:
        discount = 0

    final_amount = order_amount - (order_amount * discount / 100) 
    print(f"{order_amount} ---- {discount}% ----{final_amount}")   

    total_revenue = total_revenue + final_amount

    print("Total revenue after discounts:", total_revenue)
