import random

def final_number(name):
    print ("Okay", name, "time to choose the range.")
    low = input("Enter lowest number of the range:\t")
    high = input("Entre highest number of the range:\t")
    important_numbers = []
    while True:
        try:
            val1 = low
            val2 = high
            if val2 > val1:
                final_answer = random.randint(val1, val2)
                important_numbers = [val1, val2, final_answer]
                print ("The number has been chosen")
                if name == 314159:
                    print (important_numbers)
                return important_numbers
            else:
                responce = random.randint(1,5)
                if responce == 1:
                    print ("Does that really make sence?")
                if responce == 2:
                    print ("Should you really be playing this game?")
                if responce == 3:
                    print ("Maybe you should let someone else play")
                if responce == 4:
                    print("Where I come from",high,"isn't bigger than", low)
                if responce == 5:
                    print ("I should make you quit after that answer")
                low = input("\nLow:\t")
                high - input("High:\t")
        except ValueError:
            print ("Apparently I need to make it more clear to enter NUMBERS")
            low = input("\nLow:\t")
            high = input("High:\t")