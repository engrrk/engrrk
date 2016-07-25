from classd import Dog


class Dog:
    my_dog = Dog('TUFFY', 6)
    your_dog = Dog('lucy', 3)
    print("My dog's name is " + my_dog.name.title() + ".")
    print("My dog is " + str(my_dog.age) + " years old.")
    my_dog.roll_over()
    print("\nYour dog's name is " + your_dog.name.title() + ".")
    print("Your dog is " + str(your_dog.age) + " years old.")
    your_dog.sit()