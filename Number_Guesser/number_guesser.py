import random

top_of_range = input("Type the top range to guess from: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print('Please type a number larger than 0.')
        quit()
else:
    print('Please type a number.')
    quit()

tries = 0

random_number = random.randint(0, top_of_range)

print(random_number)

while True:
    tries += 1

    guess = input("Make a guess: ")

    if guess.isdigit():
        guess = int(guess)
    else:
        print("Please enter a number.")
        continue

    if guess == random_number:
        if tries > 1:
            print("You got it! It took you " + str(tries) + " tries to guess the correct number!")
        else:
            print("You got it on the first try! Nice!")
        quit()
    else:
        print("Incorrect. Try again.")

