from createProducts import all_products
from classes import *


def main():
    # Greet user
    print("HELLO")
    print("Welcome to Daniel's online store!\n")

    # Testing

    # create instances of DigitalProduct
    music_video = DigitalProduct(
        20, "Music Video", 14.99, 100, 2048, "mymusiclink.com")
    album = DigitalProduct(21, "Music Album", 30.99, 150, 1024, "myalbum.com")

    # create instances of PhysicalProduct
    desk = PhysicalProduct(22, "Computer Desk", 75.99, 50, 40, "6 x 6", 15.00)
    computer = PhysicalProduct(
        23, "Apple Computer", 899.99, 200, 10, "1 x 1", 10.00)
    folder = PhysicalProduct(24, "School Folder", 5.99, 200, 1, "1 x .8", 2.00)

    # create user1 and add digital products
    user1 = User(10, "Daniel", cart=Cart(cart_items=[]))
    user1.add_to_cart(music_video)
    user1.add_to_cart(album)

    # create user2 and add physical products
    user2 = User(11, "Tim", cart=Cart(cart_items=[]))
    user2.add_to_cart(desk)
    user2.add_to_cart(computer)
    user2.add_to_cart(folder)

    # verify each users' cart
    print("User1 cart")
    user1.cart.view_cart()

    print("\nUser2 cart")
    user2.cart.view_cart()

    # Create PercentageDiscount instance and apply to user1 cart
    album_discount = PercentageDiscount(50)
    user1.cart.percent_discount(21, album_discount)

    # Create FixedAountDiscount and apply to user2 cart
    computer_discount = FixedAmountDiscount(100)
    user2.cart.fixed_discount(23, computer_discount)

    # Run checkout() on user 1
    print()
    print(user1.checkout())
    # Ensure cart is cleared
    print(user1.cart.view_cart())

    # Run checkout() on user 2
    print()
    print(user2.checkout())
    # Ensure cart is cleared
    print(user2.cart.view_cart())


if __name__ == "__main__":
    main()
