import yfinance as yf

def startup():
    greeting = "hello and welcome to the stock market! "
    print(greeting)


def chooseTicker():
    chooseTicker = input("Please type in the ticker you would like to search up for ").lower()
    print(f" you have chosen {chooseTicker}")
    return chooseTicker

def  lookUpTicker():
    tickerChosenByUsr = chooseTicker()
    tickerSymbol = yf.Ticker(f"{tickerChosenByUsr}")
    info = tickerSymbol.info
    print(info)
    return info

def main():
    startup()
    lookUpTicker()

# calling main
main()