def make_pizza(size, *topping):
    """Summarize the pizza we are about to make."""
    print("\nMaking a " + str(size) +"-inch pizza with the following toppings:")
    for topping in topping:
        print("- " + topping)