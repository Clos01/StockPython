# Python Backtester Project

Goal: Build a functional backtester, understand the process from data to results, and gain hands‑on experience with relevant tools.

## Prerequisites

- Python 3.7 or higher  
- pip

## Installation

```bash
# Clone the repo (if not already)
git clone <your-repo-url>
cd PythonProject1

# Install dependencies
pip install pandas numpy yfinance
```

## Usage

```bash
python practice.py
```

Follow the prompts to enter a ticker and date range. The script will fetch data via yfinance, display info, and show a simple DataFrame summary.

## Week 1: Laying the Foundation & Manual Construction

**Monday: Environment Setup**  
- Install Python, pandas, numpy, yfinance  
- Create project folder

**Tuesday: Data Acquisition**  
- Download SPY daily data from 2015‑01‑01 to 2024‑12‑31  
- Load into Pandas DataFrame  
- Explore with `.head()`, `.info()`, `.describe()`

**Wednesday: Strategy Coding (Part 1)**  
- Compute 50‑day and 200‑day SMAs with Pandas

**Thursday: Strategy Coding (Part 2)**  
- Generate buy/sell signals based on SMA crossover  
- Store signals in new DataFrame columns

**Friday & Weekend: Manual Backtesting Loop & Initial Metrics**  
- Loop through the DataFrame day by day  
- Simulate trades: track position (long/flat) and daily portfolio value  
- Record daily equity curve  
- Compute Total Return and CAGR

**Goal:**  
By week’s end, have a working manual backtest loop, an equity curve, and a clear understanding of each step.
