# Design System Colors
NAVY_PRIMARY = "#0D1B2A"      # Deep command navy
NAVY_SECONDARY = "#1A3A5C"    # Section headers
GOLD_ACCENT = "#C9A84C"       # Key metrics and highlights  
FOREST_GREEN = "#1B4332"      # Positive signals
THREAT_RED = "#C1121F"        # Risk and alerts
WARM_GRAY = "#6C757D"         # Secondary text
LIGHT_BG = "#F8FAFC"          # Page background
CARD_BG = "#FFFFFF"           # Card backgrounds
BORDER = "#E2E8F0"            # Card borders

# Typography settings
CHART_FONT_FAMILY = "Inter, Arial, sans-serif"

# Geopolitical Events List
EVENTS = [
    {"date": "1999-05-26", "event": "Kargil War", "category": "India-Pak", "channel": "Direct", "severity": "High"},
    {"date": "2001-12-13", "event": "Parliament Attack", "category": "India-Pak", "channel": "Direct", "severity": "High"},
    {"date": "2016-09-29", "event": "Uri Surgical Strikes", "category": "India-Pak", "channel": "Direct", "severity": "Medium"},
    {"date": "2019-02-14", "event": "Pulwama Attack", "category": "India-Pak", "channel": "Direct", "severity": "High"},
    {"date": "2019-02-26", "event": "Balakot Airstrike", "category": "India-Pak", "channel": "Direct", "severity": "High"},
    {"date": "2020-06-15", "event": "Galwan Valley Clash", "category": "India-China", "channel": "Direct", "severity": "High"},
    {"date": "2022-02-24", "event": "Russia-Ukraine War", "category": "Global", "channel": "Supply Chain", "severity": "Critical"},
    {"date": "2023-10-07", "event": "Israel-Hamas War", "category": "Middle East", "channel": "Energy", "severity": "Medium"},
    {"date": "2025-05-07", "event": "Operation Sindoor", "category": "India-Pak", "channel": "Direct", "severity": "High"},
]

# Tickers to query via yfinance
TICKERS = {
    "HAL.NS": "Hindustan Aeronautics (HAL)",
    "BEL.NS": "Bharat Electronics (BEL)",
    "BEML.NS": "BEML Limited",
    "MAZDOCK.NS": "Mazagon Dock",
    "COCHINSHIP.NS": "Cochin Shipyard",
    "BDL.NS": "Bharat Dynamics (BDL)",
    "^NSEI": "Nifty 50 Index"
}

LISTING_DATES = {
    "BDL.NS": "2018-03-23",
    "COCHINSHIP.NS": "2017-08-11",
    "MAZDOCK.NS": "2020-10-12",
    "HAL.NS": None,
    "BEL.NS": None,
    "BEML.NS": None,
    "^NSEI": None
}

# Country classifications
COUNTRIES_ALL = [
    "India", "China", "Pakistan", "United States", "Russia", 
    "France", "United Kingdom", "Israel", "Saudi Arabia", 
    "Germany", "Japan", "Australia"
]

DEFAULT_COMPARISON = ["India", "China", "Pakistan"]
