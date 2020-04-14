import random
random_number=random.randint(0,101)
print("A random number has been stored")
guess=False
while guess==False:
    number=int(input(" Input your guess: "))
    if number==random_number:
        guess=True
        print("Woila! your guess is correct.")
    else:
       print("you guessed a number less than or greater than the exact number.")

    
