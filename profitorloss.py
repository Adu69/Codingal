sale_price = int(input('Please enter the sale price in numerical form: '))
cost_price = int(input('Please enter the cost price in numerical form: '))
if sale_price == cost_price:
    print('You have not made any profit or loss')
elif sale_price > cost_price:
    profit = sale_price - cost_price
    print('You have made a profit of Rs.',profit)
else:
    loss = cost_price - sale_price
    print('You have lost Rs.',loss)