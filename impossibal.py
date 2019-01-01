import random

def user_guess(low, high, answer, user_guesses):
    test = input("\nWhat number will you guess:\t")
    while True:
        try:
            guess = int(test)
            if guess > low and guess < high:
                if guess == answer:
                    return "user"
                elif guess > answer:
                    print ("Your guess was to high")
                    if guess < user_guesses[1]:
                        user_guesses[1] = guess
                    return False
                elif guess < answer:
                    print ("Your guess was to low")
                    if guess > user_guesses[0]:
                        user_guesses[0] = guess
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

def cpu_guess(answer,cpu_lst, user_lst):
    if user_lst[0] > cpu_lst[0]:
        if user_lst[1] < cpu_lst[1]:
            guess = int((user_lst[0] + user_lst[1]) /2)
        if user_lst[1] >= cpu_lst[1]:
            guess = int((user_lst[0] + cpu_lst[1]) / 2)
    if user_lst[0] <= cpu_lst[0]:
        if user_lst[1] < cpu_lst[1]:
            guess = int((cpu_lst[0] + user_lst[1]) / 2)
        if user_lst[1] >= cpu_lst[1]:
            guess = int((cpu_lst[0] + cpu_lst[1]) / 2)
    if (guess - answer) >= -5 and  (guess - answer) <= 5:
        print ("I'm close")
    if (guess - answer) >= -5 and  (guess - answer) <= 5:
        print ("I'm within 5")
    if guess < answer:
        print ("I was wrong")
        cpu_lst[0] = guess
        return False
    if guess > answer:
        print ("I was wrong")
        cpu_lst[1] = guess
        return False
    if guess == answer:
        return "cpu"

def main(lst):
    counter = 1
    chance = random.randint(0,10)
    cpu_guesses = [lst[0], lst[1]]
    user_guesses = [lst[0], lst[1]]
    while True:
        if chance < 8:
            winner = user_guess(lst[0], lst[1], lst[2], user_guesses)
            if winner != False:
                break
            winner = cpu_guess(lst[2], cpu_guesses, user_guesses)
            if winner != False:
                break
        if chance == 8 or 9:
            winner = user_guess(lst[0], lst[1], lst[2], user_guesses)
            if winner != False:
                break
            winner = cpu_guess(lst[2], cpu_guesses, user_guesses)
            if winner != False:
                break
            print ("I think I'll go again")
            winner = cpu_guess(lst[2], cpu_guesses, user_guesses)
            if winner != False:
                break
        if chance == 10:
            cpu_guesses = [lst[0], lst[1]]
            user_guesses = [lst[0], lst[1]]
        
        counter += 1
    stats = [winner, counter, "medium"]
    return stats