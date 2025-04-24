import yfinance as yf
import pandas as pd 
# from tabulate import tabulate

def startup():
    greeting = "hello and welcome to the stock market!  "
    print(greeting)


def get_ticker_input():
    tickerInput = input("Please type in the ticker you would like to search up for:  ").lower()
    print(f"You have chosen {tickerInput.upper()}") 
    return tickerInput
                          

def validate_ticker_input():
    userTicketInput = get_ticker_input()
   
    if userTicketInput == "":
        print("No Input")
        exit_program()
    else:
        ticker = yf.Ticker(userTicketInput)
        info = ticker.info
        if not info or info.get("regularMarketPrice") is None:
            print("Possible mistype for ticker or no market data found.")
            return exit_program()
        return userTicketInput

def exit_program():
    inputForExit = input("\nType 'exit' to leave program: ").lower()
    if inputForExit == "exit":
        return "you have left the program!"
    else:
        return validate_ticker_input()


def provide_info_for_ticker():
    validTicker = validate_ticker_input()
    ticker = yf.Ticker(validTicker)
    info = ticker.info
    print(info)    
    return info
    

def data_frame():

    beginningDate = input("\nPlease enter the time frame date in format (YYYY-MM-DD): ")
    lastDate = input("\nPlease enter the time frame date in format (YYYY-MM-DD): ")
    dataFormat = pd.DataFrame({"date": [beginningDate, lastDate]})
    # Converting the 'date' column to datetime
    dataFormat['date'] = pd.to_datetime(dataFormat['date'])
    # Display a preview and summary statistics
    print("\nDataFrame preview:")
    print(dataFormat.head())
    print("\nDataFrame summary:")
    print(dataFormat.describe())
    return dataFormat


def main():
    startup()
    provide_info_for_ticker()
    data_frame()
    exit_program()
# calling main
main()