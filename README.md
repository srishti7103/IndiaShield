# IndiaShield
### Strategic Defence Intelligence & Analytics Platform

[![View on Tableau Public](https://img.shields.io/badge/Tableau-View_Dashboard-E97627?style=for-the-badge&logo=tableau&logoColor=white)](https://public.tableau.com/app/profile/srishti.sharma7103/viz/IndiaShield/StrategicOverview)
[![Open in Streamlit](https://img.shields.io/badge/Streamlit-Live_App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://indiashield-h4uhwhqbpkaf9tibxlcefp.streamlit.app/)
[![Python 3.12](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Data: SIPRI](https://img.shields.io/badge/Data-SIPRI_Database-1A3A5C?style=for-the-badge)](https://www.sipri.org/databases)
[![Tableau Public](https://img.shields.io/badge/Published-Tableau_Public-E97627?style=for-the-badge&logo=tableau&logoColor=white)](https://public.tableau.com/app/profile/srishti.sharma7103/viz/IndiaShield/StrategicOverview)

---

## Overview

IndiaShield is a strategic defence analytics platform that consolidates 25 years of global military expenditure, Indian budget allocation, and arms import data into two interactive deployments — a **Tableau Public dashboard** for visual storytelling and a **Streamlit web application** for programmatic exploration.

The project answers three questions a defence analyst, policy researcher, or equity investor would care about:

- **Where does India's defence budget actually go** — modernisation or salaries?
- **How dependent is India on foreign arms suppliers**, and which supply chains are most at risk?
- **Do Indian defence stocks benefit from geopolitical escalations** or suffer alongside the broader market?

---

## Live Deployments

| Interface | Link | Best For |
|---|---|---|
| 📊 Tableau Dashboard | [View on Tableau Public](https://public.tableau.com/app/profile/srishti.sharma7103/viz/IndiaShield/StrategicOverview) | Visual storytelling, executive summary, shareable |
| 🖥️ Streamlit App | [Open Web App](https://indiashield-h4uhwhqbpkaf9tibxlcefp.streamlit.app/) | Interactive filters, deep-dive exploration, simulation |

---

## Tableau Dashboard — Published Worksheets

The Tableau workbook (`IndiaShield`) is published on Tableau Public and contains the following worksheets:

| Sheet | What It Shows |
|---|---|
| **Strategic Overview** | India's 24-year defence spend journey with geopolitical event markers; global choropleth of military expenditure |
| **Budget Anatomy** | Capital vs Revenue expenditure split (FY 2015–2025); the Modernisation Paradox trend line |
| **Regional Arms Race** | India vs China vs Pakistan absolute spend and % of GDP comparison; 10-year CAGR bar chart |
| **Arms Import Flow** | Sankey diagram — supplier-to-category flow of India's arms imports by SIPRI TIV volume |
| **Market Intelligence** | Cumulative return event study for 6 Indian defence equities across 9 geopolitical escalation events |

---

## Arms Import Flow — Sankey Diagram

The chart below maps how India's arms imports flow from **supplier countries** (left) to **weapon categories** (right), proportional to SIPRI Trend Indicator Value (TIV). Russia's dominance across Aircraft (70% of combat fleet) and Tanks/AFV (85% of armoured inventory) is immediately visible.

![Arms Import Flow Sankey](assets/sankey_diagram.png)

> **Source:** SIPRI Arms Transfers Database · Annual average TIV · 2000–2024  
> **Note:** TIV measures military capability transferred, not contract cash value. Russia's 45% total share represents the single largest supply chain concentration in India's defence ecosystem.

---

## Analytical Modules

### Module 1 — Strategic Overview
Renders India's defence spend trajectory from 2000 to 2024 (constant 2022 USD) with vertical markers for key geopolitical events — Kargil (1999), Galwan (2020), Ukraine War (2022), and Operation Sindoor (2025). A global choropleth contextualises India's spend against all major military powers.

**Key KPIs displayed:** Total budget ($86.1 Bn, 2024) · % of GDP (~2.4%) · Global rank (#4) · Capital/Revenue split · Regional gap vs China

---

### Module 2 — Budget Anatomy
Dissects India's Union Budget defence allocation (FY 2015–16 to FY 2024–25) into four spending streams: Capital Expenditure (modernisation & acquisition), Revenue Expenditure (salaries, operations), DRDO R&D, and Pension/Salary. Tracks capital utilisation rates and DRDO budget trends year-on-year.

**Core finding — The Modernisation Paradox:**

> India's total defence budget grew **5× in constant dollar terms** between 2000 and 2024. Yet the share going to Capital Expenditure — actual weapons acquisition — fell from **38.3% (FY 2016) to 28.9% (FY 2025)**. Of every ₹100 allocated to defence, only ₹29 buys new military capability. The remainder services manpower, operations, and pensions.

---

### Module 3 — Regional Arms Race
Enables dynamic comparison of military expenditure across 12 countries (India, China, Pakistan, USA, Russia, France, UK, Israel, Saudi Arabia, Germany, Japan, Australia) on two metrics: absolute spend in constant 2022 USD and spend as a percentage of GDP. Includes a 10-year CAGR chart and an India–China absolute gap tracker.

**Core finding — The China Gap:**

> In 2000, China spent 2.1× India's defence budget. By 2024, that ratio is **3.7×** ($318 Bn vs $86.1 Bn). China's budget grew **9.6× in constant terms** over 24 years while India's grew 5.4×. The gap in absolute spend widened from ~$17 Bn to ~$232 Bn.

---

### Module 4 — Arms Import Flow (Sankey)
Visualises the volume flow of India's arms imports from each supplier country into each weapon category using SIPRI TIV data. The Sankey diagram (embedded above and in the Tableau dashboard) makes supply chain concentration patterns immediately visible — which supplier dominates which category, and by how much.

**Supplier breakdown by total TIV share:**

| Supplier | TIV Share | Primary Categories |
|---|---|---|
| Russia | 45% | Aircraft, Tanks/AFV, Missiles |
| France | 11% | Aircraft (Rafale), Submarines (Scorpene) |
| USA | 9% | Transport/Maritime Aircraft, Helicopters |
| Israel | 9% | Missiles (Barak-8), Electronics (Phalcon) |
| UK | 5% | Trainer Aircraft (Hawk) |
| Others | 21% | Mixed |

---

### Module 5 — Market Intelligence
Applies an **event study methodology** to measure cumulative returns of 6 Indian defence equities — HAL, BEL, BEML, Mazagon Dock, Cochin Shipyard, Bharat Dynamics — in a ±30 trading day window around 9 geopolitical escalation events. Alpha is computed as the stock's cumulative return minus the Nifty 50 benchmark.

**Core finding — Defence Stocks as Geopolitical Hedges:**

> Indian defence equities generate positive average returns in the 30 days following high-severity border escalation events (Galwan, Balakot, Pulwama), while the Nifty 50 index declines. HAL and BEL show the strongest positive alpha — consistent with accelerated defence procurement expectations after escalations.

**Events studied:** Kargil War · Parliament Attack · Uri Surgical Strikes · Pulwama Attack · Balakot Airstrike · Galwan Valley Clash · Russia-Ukraine War · Israel-Hamas War · Operation Sindoor

---

## Key Strategic Findings

| Finding | Data Point |
|---|---|
| **Modernisation Paradox** | Capital share of defence budget: 38.3% (FY16) → 28.9% (FY25) despite 5× budget growth |
| **The China Gap** | China spends 3.7× India's budget in 2024; ratio was 2.1× in 2000 |
| **Supplier Concentration** | Russia supplies 45% of TIV; 68% of IAF combat fleet and 85% of tank inventory are Russian-origin platforms |
| **Indigenisation Progress** | Domestic procurement share: ~40% (2014) → ~65% (2024) under Make in India |
| **Defence Equity Hedge** | HAL/BEL generate positive alpha post-escalation while broader market declines |

---

## Data Sources

| Dataset | Source | Coverage |
|---|---|---|
| Military Expenditure | [SIPRI MILEX Database](https://www.sipri.org/databases/milex) | 12 countries · 2000–2024 · Constant 2022 USD |
| Arms Transfers (TIV) | [SIPRI Arms Transfers Database](https://www.sipri.org/databases/armstransfers) | India imports by supplier & category · 2000–2024 |
| Defence Budget | [Ministry of Finance — Union Budget](https://www.indiabudget.gov.in/) | Statement 6 · FY 2015–16 to FY 2024–25 |
| Equity Prices | [Yahoo Finance via yfinance](https://finance.yahoo.com/) | HAL, BEL, BEML, MAZDOCK, COCHINSHIP, BDL · 2016–2026 |

> **Data note:** For the hosted Streamlit demo, built-in verified estimates are used as fallback when raw SIPRI files are absent. All estimates are cross-referenced against published SIPRI summary reports and directionally accurate. To run with full SIPRI source data, follow the setup instructions below and place downloaded files in `data/raw/`.

---

## Repository Structure

```
IndiaShield/
├── app.py                          # Streamlit entry point & sidebar router
├── requirements.txt                # Python dependencies
├── README.md                       # Project documentation
├── research_notes.md               # Analytical parameter justifications
├── assets/
│   └── sankey_diagram.png          # Arms import flow Sankey (static export)
├── data/
│   ├── raw/                        # Source spreadsheets
│   │   ├── union_budget.csv        # Union Budget allocation data
│   │   ├── geopolitical_events.csv # Geopolitical event chronology
│   │   └── README_data.txt         # SIPRI manual download instructions
│   └── processed/                  # Formatted long-form CSV caches
│       ├── master_defence.csv      # Military expenditure (all countries, all years)
│       ├── budget_breakdown.csv    # India budget split by FY
│       └── stock_events.csv        # Daily equity prices 2016–2026
├── utils/
│   ├── constants.py                # Design tokens, color codes, event lists
│   ├── styling.py                  # CSS injector and KPI card components
│   └── charts.py                   # All Plotly chart functions (~1,200 lines)
└── modules/
    ├── data_loader.py              # Unified data loader with 3-tier fallback
    ├── overview.py                 # Module 1 — Strategic Overview
    ├── budget_analysis.py          # Module 2 — Budget Anatomy
    ├── arms_race.py                # Module 3 — Regional Arms Race
    ├── sids_calculator.py          # Module 4 — Arms Import Flow & Sankey
    └── market_intelligence.py      # Module 5 — Market Intelligence
```

---

## Local Setup

```bash
# Clone the repository
git clone https://github.com/srishti7103/IndiaShield.git
cd IndiaShield

# Install dependencies
pip install -r requirements.txt

# Launch the Streamlit app
streamlit run app.py
```

The application runs fully offline using built-in fallback data. No API keys or external services are required for local execution.

---

## Tech Stack

| Layer | Technology |
|---|---|
| Dashboard (primary) | Tableau Public |
| Web Application | Python · Streamlit |
| Visualisation | Plotly (Sankey, choropleth, radar, treemap, gauge) |
| Data Processing | Pandas · NumPy |
| Market Data | yfinance (NSE equities) |
| Caching | Streamlit `@st.cache_data` |
| Deployment | Streamlit Community Cloud |

