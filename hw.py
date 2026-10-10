ImportNumber = 27

guesses = 5

while guesses > 0:

    guesses -= 1

    guess = int(input("Guess a number between 1 and 50: "))

    if guess == ImportNumber:
        print("Congratulations! You guessed the correct number.")
        break

    elif guess < ImportNumber:
        difference = ImportNumber - guess

        if difference >= 15:
            print("🧊 Ice cold!")
        elif difference >= 8:
            print("🥶 Cold!")
        elif difference >= 4:
            print("🌡️ Warm!")
        else:
            print("🔥 Hot!")

    else:
        difference = guess - ImportNumber

        if difference >= 15:
            print("🧊 Ice cold!")
        elif difference >= 8:
            print("🥶 Cold!")
        elif difference >= 4:
            print("🌡️ Warm!")
        else:
            print("🔥 Hot!")

    print("Remaining lives:", end=" ")

    for i in range(guesses):
        print("❤️", end=" ")

    print()

if guesses == 0 and guess != ImportNumber:
    print("Sorry, you've run out of guesses.")
    print("The correct number was", ImportNumber)