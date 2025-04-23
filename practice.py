import yfinance as yf

def startup():
    greeting = "hello and welcome to the stock market!  "
    print(greeting)


def tickerInput():
    tickerInput = input("Please type in the ticker you would like to search up for:  ").lower()
    print(f"You have chosen {tickerInput.upper()}") 
    return tickerInput

#  I want to be able to check to see if the user didnt type anything dumb 

def validateTickerInput():
    userTicketInput = tickerInput()
    if userTicketInput == "":
        exitProgram()
    else:
       return userTicketInput

def exitProgram():
    inputForExit = input("Type 'exit' to leave program:  ").lower()
    if inputForExit == "exit":
        return "you have left the program!"
    else:
        return validateTickerInput()


def  lookUpTicker():
    tickerChosenByUsr = validateTickerInput()
    tickerSymbol = yf.Ticker(f"{tickerChosenByUsr}")
    info = tickerSymbol.info
    print(info)
    return info

def main():
    startup()
    lookUpTicker()

# calling main
main()