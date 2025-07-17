import random
secret_number = random.randint(1, 10)
print("guess the number to win")
while True :
     guess = int(input("enter your guessed number: "))
     if guess == secret_number:
         print("Congratulations! You guessed the number.")
         break
     elif guess< secret_number:
         print("Too low! Try again.")
     else:
         print("Too high! Try again.")
print("Thanks for playing the Number Guessing Game!")