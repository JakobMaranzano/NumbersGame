import random

def user_guess(low, high, answer):
    test = input("What number will you guess:\t")
    while True:
        try:
            guess = int(test)
            if guess > low and guess < high:
                if guess == answer:
                    return "user"
                elif guess > answer:
                    print ("Your guess was to high")
                    return False
                elif guess < answer:
                    print ("Your guess was to low")
                    return False
            else:
                responce = random.randint(1, 3)
                if responce == 1:
                    print("It might be usefull to pick a number within the range")
                if responce == 2:
                    if guess > high:
                        print ("A number below", high, "would help")
                    if guess < low:
                        print ("A number above", low, "would help")
                if responce == 3:
                    print ("Your lucky on the next level I wont let you retry")
                test = input("Please make a guess within the range:\t")
        except ValueError:
            print ("Your lucky your on easy")
            test = input("Please enter a NUMBER:\t")

def cpu_guess(answer,lst):
    guess = int((lst[0] + lst[1])/2)
    if guess < answer:
        print ("I guessed", guess, "and was to low")
        lst[0] = guess
        return False
    if guess > answer:
        print ("I guessed", guess, "and was to high")
        lst[1] = guess
        return False
    if guess == answer:
        return "cpu"

def main(lst):
    counter = 1
    cpu_guesses = [lst[0], lst[1]]
    while True:
        winner = user_guess(lst[0], lst[1], lst[2])
        if winner != False:
            break
        winner = cpu_guess(lst[2], cpu_guesses)
        if winner != False:
            break
        counter += 1
    stats = [winner, counter, "medium"]
    return stats