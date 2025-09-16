import random
print("Dice Rolling Simulator")
# print("Type roll to roll the dice")
while True:
    choose=input("Type roll to roll the dice: ").lower() 

    if choose== "roll":
        number=random.randint(1,6)
        print(f"You rolled: {number}")
    elif choose=="exiit":
        print("Ok")
        break
    else:
        print("Please enter valid text")