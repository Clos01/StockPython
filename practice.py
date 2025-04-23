import yfinance as yf


# i want to create it where the user can input the ticker they want to know about
# i want to create it where the user can input the ticker they want to know about

def startup():
    greeting = "hello and welcome to the stock market! "
    print(greeting)


def chooseTicker():
    chooseTicker = input("Please type in the ticker you would like to search up for ")
    print(chooseTicker)
    return chooseTicker

def  lookUpTicker():
    tickerChosenByUsr = chooseTicker()
    tickerSymbol = yf.Ticker(f"{tickerChosenByUsr}")
    info = tickerSymbol.info
    # info = ickerSymbol.info
    print(info)
    return info

# ticker = yf.Ticker("aapl")


# info = ticker.info

def main():
    startup()
    lookUpTicker()

# calling main
main()