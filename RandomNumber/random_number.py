import random

random_number = random.randint(1, 10)
counter = 5
while 1 <= counter:
    user_choices = int(input("Enter your choice (1-10): "))
    if user_choices == random_number:
        print("You win :))")
        break
    else:
        print("You lose :))")
        counter -= 1
print("Your score is : ", counter)