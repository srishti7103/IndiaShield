# IndiaShield 🛡️
### Strategic Defence Intelligence & Security Analytics Platform

[![Python 3.12](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B.svg)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 🔗 Live Deployment
Deploy live on Streamlit Cloud: **[Insert Your Deployed Streamlit URL Here]**

---

## 📝 Executive Summary
**IndiaShield** is a professional-grade strategic intelligence dashboard designed to monitor and analyze India's defence ecosystem. By consolidating disparate datasets—ranging from international arms transfer records to national union budget spreadsheets and stock market indices—the platform provides policy analysts, security researchers, and strategic advisors with real-time, interactive data-driven insights.

Through interactive visualization pipelines, IndiaShield maps 25 years of subcontinent military expenditures, dissects capital-vs-revenue allocation paradoxes, monitors absolute budget gaps between regional powers, and evaluates how domestic defence equities behave as market hedges during geopolitical border escalations.

---

## 🚀 Core Features (Dashboard Modules)

The platform is organized into five functional modules accessible via the sidebar navigation:

1. **🏠 Strategic Overview:** Renders a 24-year spend trajectory of India, dynamic global expenditure choropleths (world map), and five core high-level KPIs representing national ranking, expenditure-to-GDP ratios, and supply-chain risk scores.
2. **💰 Budget Anatomy:** Visualizes India's Union Budget allocation trends (FY16 to FY25), showing the relationship between Revenue (operational costs) and Capital (modernisation & acquisition) allocations, capital utilisation indices, and DRDO R&D trends.
3. **⚔️ Regional Arms Race:** Compare timeline trajectories (absolute budgets and % of GDP) dynamically for any combination of regional powers (India, China, Pakistan, USA, etc.) along with 10-year CAGR performance and a dynamic China-India spending gap tracker.
4. **🎯 Import Vulnerability (SIDS):** Computes India's dependency score against global arms suppliers using a custom mathematical model. Features interactive tabs showing an **Arms Flow Sankey Pipeline** (volume flow from suppliers to weapon categories) and a **Radar Risk Fingerprint** mapping supplier vulnerability profiles. Includes a collapsible **Simulation Sandbox** to model geopolitical shifts.
5. **📈 Market Intelligence:** Explores 6 Indian defence equities (HAL, BEL, BEML, Mazagon Dock, Cochin Shipyard, Bharat Dynamics) during escalation events (e.g. Galwan, Balakot) using event study cumulative returns, outperformance alpha bar charts, and historical price history overlays.

---

## 🔬 The SIDS Metric Formulation
The **Strategic Import Dependency Score (SIDS)** is a novel composite metric developed for IndiaShield that measures India's vulnerability to supply chain disruptions from individual arms suppliers:

$$SIDS = \frac{IC}{100} \times SSR \times (1 - GSS) \times \frac{1}{DSC} \times 100$$

*   **Import Concentration ($IC$):** The percentage of total arms import volume (TIV) sourced from the supplier.
*   **Single-Source Risk ($SSR$):** Measures platform dependency. A weighted score reflecting supplier lock-in (having $>60\%$ share in a critical weapon category = $1.0$, $>40\%$ = $0.6$, else $0.2$).
*   **Geopolitical Stability ($GSS$):** Supplier reliability on a scale of $0.0$ to $1.0$ ($0.0$ = high sanction/embargo risk, $1.0$ = fully integrated ally).
*   **Substitution Capacity ($DSC$):** Local indigenisation capacity to replace the supplier's technology ($0.1$ = irreplaceable / high-tech lock-in, $1.0$ = immediate domestic replacement).

---

## 📁 Repository Modular Structure
This project is engineered using a modular, decoupled architecture rather than a single monolithic script:

```
IndiaShield/
├── app.py                      # Application entry point & sidebar router
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
├── .streamlit/
│   └── config.toml             # Custom theme configuration (Navy & Gold theme)
├── data/
│   ├── raw/                    # Source spreadsheets
│   │   ├── union_budget.csv    # Union Budget allocation metrics
│   │   ├── geopolitical_events.csv # Chronology of regional conflicts
│   │   └── README_data.txt     # Instructions for manual SIPRI downloads
│   └── processed/              # Formatted long-form CSV caches
├── utils/
│   ├── constants.py            # Design tokens, color codes, & constants
│   ├── styling.py              # CSS injector and custom KPI metric cards
│   └── charts.py               # Reusable Plotly charting functions
└── modules/
    ├── data_loader.py          # Unified data loaders and timezone handlers
    ├── overview.py             # Page 1 rendering logic
    ├── budget_analysis.py      # Page 2 rendering logic
    ├── arms_race.py            # Page 3 rendering logic
    ├── sids_calculator.py      # Page 4 rendering logic (metric calculations)
    └── market_intelligence.py  # Page 5 rendering logic
```

---

## 📊 Data & Robust Fallback Architecture
The application runs on four consolidated data pipelines:
1. **SIPRI Military Expenditure Database**
2. **SIPRI Arms Transfers Database (TIV)**
3. **Ministry of Finance (Union Budget of India)**
4. **NSE Equities Data (Yahoo Finance)**

> [!TIP]
> **Production Resilience:** The data loader in `modules/data_loader.py` is equipped with a high-fidelity synthetic fallback generator. If the app is offline or the yfinance API hits rate limits, the loader automatically interpolates historical trends and generates daily pricing arrays to ensure all 5 pages render without crash.

---

## 🛠️ Local Setup & Run

To clone and run this application locally:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/srishti7103/IndiaShield.git
   cd IndiaShield
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Launch the application:**
   ```bash
   streamlit run app.py
   ```

---

## 💡 Strategic Insights Discovered
*   **The Modernisation Paradox:** While total allocation grew 5×, the share of Capital Expenditure (modernisation & acquisitions) fell from **38.3%** in 2015 to **28.9%** in 2024, showing that manpower and pensions are squeezing acquisition power.
*   **Critical Lock-in:** Russia remains India's most critical supply-chain vulnerability with a SIDS score of **72 (Critical)**. Sanctions post-2022 mean spare-parts lifecycles for air fleets ($68\%$ Russian) and tanks ($85\%$ Russian) face severe disruption without accelerated indigenisation.
*   **Geopolitical Hedge Assets:** Indian defence equities (HAL, BEL) act as market hedges, generating average gains of **+23%** in the 30 days following border escalations while the Nifty 50 Index declines.
*   **Indigenisation Gain:** Sourcing from domestic defence companies grew from **40%** to **65%** under the Make in India initiative between 2014 and 2024.
