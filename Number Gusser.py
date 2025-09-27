            #This program is a simple number guessing game called "Number Gusser".
'''Number Guesser – Random number between 1–100, user guesses, program gives hints (“too high/too low”).'''
import random
from colorama import Fore, Style
def Number_Gusser():
    print(Fore.MAGENTA +"-- 🎉🤩🎉WELCOM TO NUMBER GUSSER--🎉🤩🎉🎉🤩🎉" + Style.RESET_ALL)
    print(Fore.CYAN + "YOU HAVE 10 ATTEMPTS TO GUEES THE CORRECT NUMBER" + Style.RESET_ALL)
    number=random.randint(1,100)
    l=7
    attempts=10
    for i in range(l):
        guess=int(input(Fore.YELLOW + "ENTER YOUR GUESS B/W 1-100:- " + Style.RESET_ALL))
        if guess<1 or guess>100:
         print(Fore.RED + "INVALID! NUMBER, IT MUST BE B/W 1-100" + Style.RESET_ALL)
         attempt=attempt-1
         continue
        if guess==number:
            print(Fore.GREEN + "\nCongrats: It's Correct Guess 🎊🏆🎊")
            break
        elif guess>number:
            print(Fore.RED + "HINT: Too High: Try again!" + Style.RESET_ALL)
            attempts=attempts-1
            
        else:
            print(Fore.RED + "HINT: Too Low: Try Again!" +Style.RESET_ALL)
            attempts=attempts-1
        print(Fore.BLUE+"Attempts Left --- ", attempts," "+Style.RESET_ALL)
    if guess!=number:
        print(Fore.RED + "Sorry: You've used all attempts. The correct number was", number, Style.RESET_ALL)

Number_Gusser()

