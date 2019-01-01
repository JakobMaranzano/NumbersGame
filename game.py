import random
import easy
import medium
import hard
import extream

def header():
    print ("="*69)
    print ("")
    print ("="*24, " THE GUESSING GAME ", "="*24)
    print ("")
    print ("="*69)
    print ("\t\t\t  WELCOME CHALENGER")
    print ("Hello, I am Ricky the one who runs this game.")
    name = str(input("What is your name?\t"))
    if name.lower() == "jakob":
        print ("Hello me. Good luck")
        name = 314159
        return name
    print ("Hello", name, "I hope you came ready to play")
    print ("\nNow what difficulty would you like to play against me on?")
    return name

def level_text():
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
    print ("Exit(6)")

def final_number(lst):
    global name
    while True:
        try:
            val1 = int(lst[0])
            val2 = int(lst[1])
            if val2 > val1:
                final_answer = random.randint(val1, val2)
                full_lst = [val1, val2, final_answer]
                print ("The number has been chosen")
                if name == 314159:
                    print (full_lst)
                return full_lst
            else:
                responce = random.randint(1,5)
                if responce == 1:
                    print ("Does that really make sence?")
                if responce == 2:
                    print ("Should you really be playing this game?")
                if responce == 3:
                    print ("Maybe you should let someone else play")
                if responce == 4:
                    print("Where I come from",lst[1],"isn't bigger than", lst[0])
                if responce == 5:
                    print ("I should make you quit after that answer")
                lst[0] = input("\nLow:\t")
                lst[1] = input("High:\t")
        except ValueError:
            print ("I hope it's a mistake that you got this message")
            low = input("\nLow:\t")
            high = input("High:\t")
            lst[0] = low
            lst[1] = high

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

def scoreboard(lst):
    global name
    easy_leaders = []
    medium_leaders = []
    hard_leaders = []
    extream_leaders = []
    impossibal_leaders = []
    print ("\nLet's see how you rank on the leader board")
    if name == 314159:
        print ("Good try cheater but your score can't be recorded if you already knew the answer")
    elif lst[2] == "easy":
        lst.pop(2)
        easy_leaders.append(lst)
        for elm in lst:
            return elm
    elif lst[2] == "meduim":
        lst.pop(2)
        medium_leaders.append(lst)
        for elm in lst:
            return elm
    elif lst[2] == "hard":
        lst.pop(2)
        hard_leaders.append(lst)
        for elm in lst:
            return elm
    elif lst[2] == "extream":
        lst.pop(2)
        extream_leaders.append(lst)
        for elm in lst:
            return elm
    elif lst(2) == "impossibal":
        lst.pop(2)
        impossibal_leaders.append(lst)
        for elm in lst:
            return elm

def easy_option(name):
    print ("="*69)
    print ("")
    print ("="*30, " EASY! ", "="*30)
    print ("")
    print ("="*69)
    print ("I'll go easy on you then")
    print ("Pick number range (I only keep scores for games if the range is 0 - 100)")
    low = input("Low:\t")
    high = input("High:\t")
    range_lst = [low, high]
    important_numbers = final_number(range_lst)
    game_over = easy.main(important_numbers)
    if game_over[0] == "user":
        print ("Congradulations", name, "You guessed the correct number. It only took you", game_over[1], "trie(s)")
        if game_over[1] >= 15:
            print ("You should play some more before moving up a level")
        if important_numbers[0] == 0 and important_numbers[1] == 100:
            game_over[0] = name
            scoreboard(game_over)
    if game_over[0] == "cpu":
        print ("How does it feel to lose to the me on easy", name)

def meduim_option(name):
    print ("="*69)
    print ("")
    print ("="*30, "MEDIUM!", "="*30)
    print ("")
    print ("="*69)
    print ("You your going to let me try a little")
    print ("Pick number range (I only keep scores for games if the range is 0 - 100)")
    low = input("Low:\t")
    high = input("High:\t")
    range_lst = [low, high]
    important_numbers = final_number(range_lst)
    game_over = medium.main(important_numbers)
    if game_over[0] == "user":
        print ("Congradulations", name, "You guessed the correct number. It only took you", game_over[1], "trie(s)")
        if game_over[1] >= 15:
            print ("You should play some more before moving up a level")
        if important_numbers[0] == 0 and important_numbers[1] == 100:
            game_over[0] = name
            scoreboard(game_over)
    if game_over[0] == "cpu":
        print ("Come on", name, "I'm hardly trying yet")

def hard_option(name):
    print ("="*69)
    print ("")
    print ("="*31, "HARD!", "="*31)
    print ("")
    print ("="*69)
    print ("Are you ready to chalenge someone with the smae knolege that you have")
    print ("Pick number range (I only keep scores for games if the range is 0 - 100)")
    low = input("Low:\t")
    high = input("High:\t")
    range_lst = [low, high]
    important_numbers = final_number(range_lst)
    game_over = hard.main(important_numbers)
    if game_over[0] == "user":
        print ("Congradulations", name, "You guessed the correct number. It only took you", game_over[1], "trie(s)")
        if important_numbers[0] == 0 and important_numbers[1] == 100:
            game_over[0] = name
            print (scoreboard(game_over))
    if game_over[0] == "cpu":
        print ("The number you were looking for was", important_numbers[2], "and I found it first")
        print ("So",name, "are you really going to let me stay the champ?")

def extream_option(name):
    print ("="*69)
    print ("")
    print ("="*31, "EXTREAM!", "="*31)
    print ("")
    print ("="*69)
    print ("Are you ready to chalenge someone with the smae knolege that you have")
    print ("Pick number range (I only keep scores for games if the range is 0 - 100)")
    low = input("Low:\t")
    high = input("High:\t")
    range_lst = [low, high]
    important_numbers = final_number(range_lst)
    game_over = extream.main(important_numbers)
    if game_over[0] == "user":
        print ("Congradulations", name, "You guessed the correct number. It only took you", game_over[1], "trie(s)")
        if important_numbers[0] == 0 and important_numbers[1] == 100:
            game_over[0] = name
            print (scoreboard(game_over))
    if game_over[0] == "cpu":
        print ("The number you were looking for was", important_numbers[2], "and I found it first")
        print ("So",name, "are you really going to let me stay the champ?")

name = header()
level_text()
option = input("\nPlease pick a number 1-6:\t")
level = checking_input(option)
while level != 6:
    if level == 1:
        easy_option(name)
    if level == 2:
        meduim_option(name)
    if level == 3:
        hard_option(name)
    if level == 4:
        extream_option(name)
    if level == 5:
        print ("work in progress")
    if level == 7:
        level_text()
    again = input("\nWould you like to play me again?(y/n)\t")
    while True:
        if again.lower() == "y":
            option = input("What level will you play me on this time?(Enter 7 to see my level description again):\t")
            level = checking_input(option)
            break
        elif again.lower() == "n":
            level = 6
            break
        else:
            "It clearly says (y/n) so please enter 'y' or 'n'"
            again = input("Would you like to play again?(y/n):\t")
print ("Bye")