from createProducts import all_products
from classes import *


def main():
    # Greet user
    print("HELLO")
    print("Welcome to Daniel's online store!\n")

    # Display current discounts in store
    print("Current Discounts:\n")
    # for each discount dict in all_dicounts
    for discount in all_discounts:
        # get the name of the discounted product
        name = [x.name for x in all_products if x.product_id ==
                discount["product_id"]][0]

        # display different messages depending on the type of dicount (percentage or fixed rate)
        if discount["type"] == "percentage":
            print(f'{name} is {discount["amount"]}% off!')
        else:
            print(f'Save ${discount["amount"]} on {name}!')

    # Testing
    """
    Product classes have already been successfully created in
    createProducts.py, however I will manually create another
    in this code for further verification.
    """
    # Create test product class
    my_product = Product(19, "Wallet", 3.99, 10)
    # test update_quantity
    print(f"\nmy_product quantity before update: {my_product.quantity}")
    my_product.update_quantity(20)
    print(f"my_product quantity after update: {my_product.quantity}\n")
    # test get_product_info
    print(my_product.get_product_info())

    # Further testing on other Product objects already instantiated
    toothpicks = all_products[0]
    print(f"\nmy_product quantity before update: {toothpicks.quantity}")
    toothpicks.update_quantity(350)
    print(f"my_product quantity after update: {toothpicks.quantity}\n")
    # test get_product_info
    print(toothpicks.get_product_info())

    """
    For testing DigitalProduct and PhysicalProduct classes, 
    I am just going to use the objects already created in 
    createProducts.py and call get_product_info() on each 
    because that will show whether or not the method was 
    successfully overridden during class creation. 
    """
    TV = all_products[3]
    print()
    print(TV.get_product_info())

    avengers = all_products[-1]
    print()
    print(avengers.get_product_info())

    """
    Cart class testing
    """
    # initialize empty cart
    my_cart = Cart()

    # add products to cart
    my_cart.add_product(TV)
    my_cart.add_product(avengers)

    # View cart contents
    print()
    my_cart.view_cart()

    # remove cart item by ID
    my_cart.remove_product(9)
    print()
    my_cart.view_cart()

    # add back item and test calculate total
    my_cart.add_product(avengers)
    print()
    print(f"Total: {my_cart.calculate_total()}")

    """
    Verifiyng that attributes in my_cart are private, 
    the following code should produce an error, so I've 
    wrapped it in a try-catch block so the program will
    continue running despite the error. 
    """
    print()
    try:
        print(my_cart.__cart_items)
    except AttributeError:
        print(f"Error! The attribute is private.")

    """
    User class testing
    """
    # Create user with empty cart
    my_user = User(1, "Daniel", cart=Cart(cart_items=[]))

    # Test add_to_cart()
    print()
    my_user.add_to_cart(TV)
    my_user.add_to_cart(all_products[0])
    print(my_user.cart.view_cart())

    # Test remove_from_cart()
    print()
    my_user.remove_from_cart(4)
    print(my_user.cart.view_cart())

    print(my_user.checkout())


if __name__ == "__main__":
    main()
