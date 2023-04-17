import pandas as pd

products = {'Oranges (packaged)': 114.99, 'Candy (Rotfront)': 280.0, 'Boiled sausage': 199.99, 'Juice J7 (orange)': 119.99, 'Trout (Seven Seas)': 399.99}
stocks = {'Boiled sausage': '33%', 'Juice J7 (orange)': '12%', 'Trout (Seven Seas)': '18%'}

def apply_discounts(products, stocks):
    for i in products:
        if i in stocks:
            disc =float((stocks.get(i))[0:-1])/100
            products.update({i:round(products.get(i)-products.get(i)*disc,2)})
    return products

print(apply_discounts(products, stocks))