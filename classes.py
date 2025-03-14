from abc import ABC, abstractmethod


class Product:
    """
    A class used to represent a product for an online store. 
    Base class for other product classes. 

    Atributes 
    ---------
    product_id: int 
        the unique ID of the product 
    name: str 
        name of the product
    price: float 
        price of the product 
    quantity: int
        total amount of product
    """

    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def update_quantity(self, new_quantity):
        """
        Updates self.quantity with a new value 

        Parameters
        ----------
        new_quantity: int 
            The new amount of the product
        """

        self.quantity = new_quantity

    def get_product_info(self):
        """
        Prints product info with all attributes to the 
        terminal
        """
        print(f'***PRODUCT INFO****')
        print(f'ID: {self.product_id}')
        print(f'NAME: {self.name}')
        print(f'PRICE: {self.price}')
        print(f'QUANTITY: {self.quantity}')


class DigitalProduct(Product):
    """
    A class used to represent a digitally available product
    in an online store. Inherits from Product class. 

    Atributes 
    ---------
    product_id: int 
        the unique ID of the product 
    name: str 
        name of the product
    price: float 
        price of the product 
    quantity: int
        total amount of product 
    file_size: int 
        the size of the file in megabytes 
    download_link: str
        link to download the item
    """

    def __init__(self, product_id, name, price, quantity, file_size, download_link):
        super().__init__(product_id, name, price, quantity)
        self.file_size = file_size
        self.download_link = download_link

    def get_product_info(self):
        """
        Prints product info with all attributes to the 
        terminal
        """
        print(f'***PRODUCT INFO****')
        print(f'ID: {self.product_id}')
        print(f'NAME: {self.name}')
        print(f'PRICE: {self.price}')
        print(f'QUANTITY: {self.quantity}')
        print(f'FILE SIZE: {self.file_size}')
        print(f'DOWNLOAD LINK: {self.download_link}')


class PhysicalProduct(Product):
    """
    A class used to represent a physically available product
    in an online store. Inherits from Product class. 

    Atributes 
    ---------
    product_id: int 
        the unique ID of the product 
    name: str 
        name of the product
    price: float 
        price of the product 
    quantity: int
        total amount of product 
    weight: float
        weight in pounds of the item
    dimensions: str
        length and width of the item
    shipping_cost: float
        cost to ship the item
    """

    def __init__(self, product_id, name, price, quantity, weight, dimensions, shipping_cost):
        super().__init__(product_id, name, price, quantity)
        self.weight = weight
        self.dimensions = dimensions
        self.shipping_cost = shipping_cost

    def get_product_info(self):
        """
        Prints product info with all attributes to the 
        terminal
        """
        print(f'***PRODUCT INFO****')
        print(f'ID: {self.product_id}')
        print(f'NAME: {self.name}')
        print(f'PRICE: {self.price}')
        print(f'QUANTITY: {self.quantity}')
        print(f'WEIGHT: {self.weight}')
        print(f'DIMENSIONS: {self.dimensions}')
        print(f'SHIPPING COST: {self.shipping_cost}')


class Cart():
    """
    A class used to represent a shopping cart in an 
    online store. 

    Attributes
    ----------
    cart_items: list 
        list of Product objects 
    """

    def __init__(self, cart_items=[]):
        self.__cart_items = cart_items

    def add_product(self, product):
        """
        Adds a Product object to cart_items

        Parameters
        ----------
        product: Product object 
            an available product
        """
        self.__cart_items.append(product)

    def remove_product(self, product_id):
        """
        Removes a product from cart_items

        Parameters
        ----------
        product_id: int
            ID of the product to remove
        """
        for item in self.__cart_items:
            if item.product_id == product_id:
                self.__cart_items.remove(item)

    def view_cart(self):
        """
        Prints all the items currently in the cart
        """
        print("***ITEMS IN CART***")
        if len(self.__cart_items) != 0:
            for item in self.__cart_items:
                print(f'{item.name}')
        else:
            print("Your cart is empty.")

    def calculate_total(self):
        """
        Applies available discounts to all items in the cart
        and calculates the total.

        Returns
        -------
        total: float 
            total price of all items in cart after discounts
        """
        total = 0

        # calculate total after applying discount
        for item in self.__cart_items:
            total += item.price

        return total

    def percent_discount(self, prodcut_id, discount):

        for item in self.__cart_items:
            if item.product_id == prodcut_id:
                item.price = discount.apply_discount(item.price)

    def fixed_discount(self, product_id, discount):

        for item in self.__cart_items:
            if item.product_id == product_id:
                item.price = discount.apply_discount(item.price)


class User:
    """
    A class to represent a user in an online store

    Attributes
    ----------
    user_id: int 
        unique user_id to identify the user
    name: str
        name of the user 
    cart: Cart 
        Cart object to store user products
    """

    def __init__(self, user_id, name, cart: Cart):
        self.user_id = user_id
        self.name = name
        self.cart = cart

    def add_to_cart(self, product):
        """
        Adds items to the users cart using cart.add_product()

        Parameters
        ----------
        product: Product object 
            Product to be added to cart
        """
        self.cart.add_product(product)

    def remove_from_cart(self, product_id):
        """
        Removes item from cart using car.remove_product()

        Parameters
        ----------
        product_id: int 
            product to be removed
        """
        self.cart.remove_product(product_id)

    def checkout(self):
        """
        Calculates total price of all items and clears
        the user cart. 
        """
        total = self.cart.calculate_total()
        self.cart = Cart(cart_items=[])

        return total


class Discount(ABC):
    """
    Abstract class that acts as blueprint for other 
    discount calsses
    """
    @abstractmethod
    def apply_discount(self, total_amount):
        pass


class PercentageDiscount(Discount):
    """
    Class that calculates the dicount on an item given a 
    percentage

    Attributes
    ----------
    percentage: float
        percent value for discount
    """

    def __init__(self, percentage):
        self.percentage = percentage

    def apply_discount(self, total_amount):
        """
        Applies the percent discount given a total amount

        Parameters
        ----------
        total_amount: float 
            total dollar amount before discount 

        Returns
        -------
        The total dollar amount after discounts are appplied rounded
        to 2 decimal places.
        """
        # Convert percentage to a decimal
        discount = self.percentage / 100

        # return total amount with discount applied
        return round((total_amount - (total_amount * discount)), 2)


class FixedAmountDiscount(Discount):
    """
    Class that calculates dicount on an item given a fixed
    amount

    Attributes 
    ----------
    amount: float 
        amount to be discounted
    """

    def __init__(self, amount):
        self.amount = amount

    def apply_discount(self, total_amount):
        """
        Applies dicount to a given dollar ammount

        Parameters
        ----------
        total_amount: float 
            Total dollar amount before dicount 

        Returns 
        -------
        Total dollar amount minus the discount. 
        """
        # return total amount with discount applied
        return total_amount - self.amount
