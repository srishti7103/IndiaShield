"""
Run this script ONCE locally to download real NSE stock data.
It replaces the simulated stock_events.csv with actual prices from Yahoo Finance.

Usage:
    python fetch_real_data.py

Requirements:
    pip install yfinance
"""

import yfinance as yf
import pandas as pd
from pathlib import Path

OUTPUT = Path("data/processed/stock_events.csv")
OUTPUT.parent.mkdir(parents=True, exist_ok=True)

TICKERS = [
    "HAL.NS",
    "BEL.NS",
    "BEML.NS",
    "MAZDOCK.NS",
    "COCHINSHIP.NS",
    "BDL.NS",
    "^NSEI",          # Nifty 50 benchmark
]

print("Downloading NSE equity data from Yahoo Finance...")
print(f"Tickers: {TICKERS}")
print("Period : 2016-01-01 -> 2026-01-01")
print()

df = yf.download(
    TICKERS,
    start="2016-01-01",
    end="2026-01-01",
    auto_adjust=True,
    progress=True
)["Close"]

# Per-column forward-fill within trading history (leaving everything before first trading day as NaN)
for col in df.columns:
    first_valid = df[col].first_valid_index()
    if first_valid is not None:
        df.loc[first_valid:, col] = df.loc[first_valid:, col].ffill()
df.index.name = "Date"

df.to_csv(OUTPUT)
print(f"\nSaved {len(df)} rows x {len(df.columns)} columns -> {OUTPUT}")
print("\nColumn check:")
for col in df.columns:
    non_null = df[col].notna().sum()
    print(f"  {col:20s}  {non_null} trading days")
