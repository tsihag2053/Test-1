ImportNumber = 27
guesses = 5
while guesses > 0:
    guesses -= 1
    guess = int(input("Guess a number between 1 and 50: "))
    if guess == ImportNumber:
        print("Congratulations! You guessed the correct number.")
        break
    elif guess < ImportNumber:
        print("Your guess is too low. Try again.")
    else:
        print("Your guess is too high. Try again.")

i = "*****"
for i in range(5-i):
    print("*" * (i + 1))

if guesses == 0:
    print("Sorry, you've run out of guesses. The correct number was", ImportNumber)
    