# Guessing game challenge

from random import randint
num = randint(1,100)

# no of guesses a palyer makes
guesses = [0]

while True:

	guess_no = int(input("what's your guess: "))

	if guess_no < 1 or guess_no > 100:
		print("OUT OF BOUNDS.Please try again: ")
		continue
	

	guesses.append(guess_no)


	if guesses[-2]:
		if abs(num-guess_no) < abs(num-guesses[-2]):
			print("WARMER!")
		else:
			print("COLDER!")
	else:
		if abs(num-guess_no) <= 10:
			print("WARM!!")
		else:
			print("COLD!!")


	if num == guess_no:
		print(f"CONGRATULATIONS!,YOU GUESSES IN {len(guesses)-1} GUESSES.")
		break