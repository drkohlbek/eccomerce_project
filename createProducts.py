"""
This program instatiates products from .csv files and creates discounts to be used in main.py
"""
import csv
from classes import Product, PhysicalProduct, DigitalProduct

# Normal products
products = []
with open('products.csv', 'r') as products_csv:
    reader = csv.DictReader(products_csv)
    # for each line in csv
    for line in reader:
        # create product object and append to list
        product_id, name, price, quantity = line.values()
        products.append(Product(int(product_id), name,
                        float(price), int(quantity)))

# assign variable names to each object in list
toothpick, leash, folder = products

# Physical products
physical_products = []
with open('physical_products.csv', 'r') as products_csv:
    reader = csv.DictReader(products_csv)
    # for each line in csv
    for line in reader:
      # create physical product object and append to list
        product_id, name, price, quantity, weight, dimensions, shipping_cost = line.values()
        physical_products.append(
            PhysicalProduct(int(product_id), name, float(price), int(quantity), float(weight), dimensions, float(shipping_cost)))

TV, iphone, watch = physical_products

# Digital products
digital_products = []
with open('digital_products.csv', 'r') as products_csv:
    # for each line in csv
    reader = csv.DictReader(products_csv)
    for line in reader:
      # create digital product object and append to list
        product_id, name, price, quantity, file_size, download_link = line.values()
        digital_products.append(
            DigitalProduct(int(product_id), name, float(price), int(quantity), int(file_size), download_link))

animation, art, avengers = digital_products


# list of all products to export
all_products = [toothpick, leash, folder, TV,
                iphone, watch, animation, art, avengers]
