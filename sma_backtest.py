# Import necessary libraries
import backtrader as bt
import yfinance as yf
import pandas as pd
import datetime
import matplotlib.pyplot as plt # Often imported like this for plotting

class MyStrategy(bt.Strategy):
        def next(self):
            pass 
cerebo = bt.Cerebro()

cerebo.addstrategy(MyStrategy)

cerebo.run()

