'''   ---Stock Returns Calculator---   '''

from colorama import Fore, Style                                                        #Importing colorma for colored terminal text
def Stock_returns_calculator():
    print(Fore.CYAN + Style.BRIGHT + "\n \t\t---Welcome to Stock Returns Calculator---" + Style.RESET_ALL)
    try:
    #Take input for buy price, sell price and no of shares
        buy_price = float(input(Fore.YELLOW+ "Buy Price   : " + Style.RESET_ALL))
        sell_price = float(input(Fore.YELLOW + "Sell Price  : " + Style.RESET_ALL))
        shares=int(input(Fore.YELLOW +"Quantity    : "+Style.RESET_ALL))
    
        returns= sell_price - buy_price
        total_returns= (returns*shares)                                                   #Calcuates total reurns based on number of shares
        percentage_returns=((returns/buy_price)*100)                                    #Calculates percentage returns

    #Adding layers to display profit in green, loss in red and brek-even in yellow.   
    
        def print_result(label, value):
            if value>0:
                print(Fore.GREEN + Style.BRIGHT + f"{label} {value:.2f}"+ Style.RESET_ALL)   #Displays Profit in Green
            elif value<0:
                print(Fore.RED + Style.BRIGHT + f"{label} {value:.2f}"+ Style.RESET_ALL)     #Displays Loss in Red
            else:
                print(Fore.YELLOW + Style.BRIGHT + f"{label} {value}"+ Style.RESET_ALL)  #Displays Break-even in Yellow

        print_result("Absolute P/L: ", total_returns)  
        print_result("Return      : ", percentage_returns)
        
    #If user enters a non-numeric value, error message wil be displayed in red. 
    
    except ValueError:
        print(Fore.RED +"Invalid input, please enter a nummeric value." + Style.RESET_ALL)

#Calling the Function to run the calculator
Stock_returns_calculator()