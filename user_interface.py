import random

def welcome():
    print ("="*69)
    print ("")
    print ("="*24, " THE GUESSING GAME ", "="*24)
    print ("")
    print ("="*69)
    print ("Welcome to the guessing game")
    name = input("What name would you like to go by?:\t")
    correct = input("Is this the name you want to go by?(y/n):\t")
    counter = 1
    while correct.lower() == "n":
        name = input("Well what is your correct name then?:\t")
        counter += 1
        correct = input("Is this your correct name?:\t")
    if correct.lower() != "y":
        print ("I asked for 'y' or 'n' but I'll take", correct, "as yes")
    if counter > 3:
        print ("This might not be the right game for you if it took", counter, "time to enter your name")
    print ("\nAlright", name, "I have jest a few more questions to ask you.")
    first_time = input("Is this your first time playing?(y/n):\t")
    if first_time.lower() == "y":
       print ("\nWell welcome again to the guessing game")
       print ("My name is Ricky and I will be the one your playing against today")
       print ("The rules are as follows:")
       print ("1. You will be able to pick what difficulty I will play you as")
       print ("2. You will be able to pick the lowest and the highest number")
       print ("3. The computer will pick a random number from that range")
       print ("4. We will then take turns guessing what that number is")
       print ("5. First one to get tht number wins")
    print ("\nOkay then", name, "time to pick the difficulty")
    return name

def difficulty_menu():
    print ("\nEasy(1):")
    print ("-Random guessing\n-Does not use your input\n-Shows my guesses")
    print ("Meduim(2):")
    print ("-Smart guessing\n-Does not use your input\n-Shows my guesses")
    print ("Hard(3):")
    print ("-Smart guessing\n-Uses your input\n-Show my guesses")
    print ("Extream(4):")
    print ("-Smart guessing\n-Uses your input\n-Does not show my guesses")
    print ("Impossibal(5):")
    print ("-You'll have to play me to find out")
    print ("Show scorebaord(6)")
    print ("Exit(7)")

def exit():
    print("Bye!")

def checking_input(option):
    while True:
        try:
            test = int(option)
            if test >= 1 and test <= 7:
                return test
            else:
                responce = random.randint(1,5)
                if responce == 1:
                    print ("Does that really make sence?")
                if responce == 2:
                    print ("Should you really be playing this game?")
                if responce == 3:
                    print ("Maybe you should let someone else play")
                if responce == 4:
                    print("Please enter a number within the range")
                if responce == 5:
                    print ("I should make you quit after that answer")
                option = input("\nEnter a number between 1 AND 6:\t")
        except ValueError:
            responce = random.randint(1,6)
            if responce == 1:
                print ("Does that really make sence?")
            if responce == 2:
                print ("Should you really be playing this game?")
            if responce == 3:
                print ("Maybe you should let someone else play")
            if responce == 4:
                print("Please enter a number this time")
            if responce == 5:
                print ("I should make you quit after that answer")
            option = input("\nEnter a NUMBER between 1 and 6:\t")

def main():
    name = welcome()
    difficulty_menu()
    option = input("\nSo what level will it be?:\t")
    level = checking_input(option)
    while level != 7:
        if level == 1:
            easy.main(name)
        if level == 2:
            medium.main(name)
        if level == 3:
            hard.main(name)
        if level == 4:
            extream.main(name)
        if level == 5:
            impossibal.main(name)
        if level == 6:
            print ("Score board")
    exit()

if __name__ == "__main__":
    main()