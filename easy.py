import random
import winning_number as WN

def header(name):
    print ("="*69)
    print ("")
    print ("="*30, " EASY! ", "="*30)
    print ("")
    print ("="*69)
    print ("Okay", name, "I'll go easy on you then")

def user_turn(low, high, answer):
    entered_statement = input("What number do you think it is?:\t")
    while True:
        try:
            guess = int(entered_statement)
            if guess > low and guess < high:
                if guess ==  answer:
                    return "user"
                if guess < answer:
                    print (guess ,"is below the answer")
                    return "continue"
                if guess > answer:
                    print (guess< "is above the answer")
                    return "continue"
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
                print ("Your answer has to be between", low, "and", high)
                entered_statement = input("Please give a VALID guess:\t")
        except ValueError:
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
                print ("Your answer has to be a NUMBER")
                entered_statement = input("Please enter a VALID guess:\t")

def main(name):
    header(name)
    important_numbers = WN.final_number(name)
    while winner == "continue"
