import random
number=random.randint(1,100)
print("GUESS A NUMBER FROM 1 TO 100")
tries=0
while True:
    guess=int(input("ENTER YOUR GUESS:"))
    tries+=1
    if guess>number:
        print("YOUR GUESS IS TOO HIGH:")
    elif guess<number:
        print("GUESS IS TOO LOW:")
    else:
        print(f"CONGRATULATIONS YOU GUESSED THE NUMBER {number} IN {tries} TRIES!")
    break