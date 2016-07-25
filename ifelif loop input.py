height = input("How tall are you, in inches? ")
height = int(height)
if height<=18:
    print("\nYou're not tall enough to ride!")
elif 18<= height<=36:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")