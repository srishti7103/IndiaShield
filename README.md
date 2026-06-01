# IndiaShield 🛡️
India's Strategic Defence Intelligence Platform

## Live App
[Link to Streamlit deployment]

## What This Project Does
IndiaShield is a professional-grade strategic intelligence dashboard designed to monitor and analyze India's defence ecosystem. It brings together multi-dimensional datasets covering military expenditures, Union Budget details, regional arms races, supplier-level vulnerabilities, and financial market reactions. By consolidating these disparate datasets, the platform provides policy analysts, defence researchers, and strategic advisors with real-time, interactive insights.

Through interactive visualization pipelines, IndiaShield maps 25 years of spending trends, dissects capital versus revenue budget paradoxes, monitors the widening absolute spending gap in the subcontinent, and evaluates the performance of Indian defence equities during military escalation events.

## The SIDS Metric (Novel Contribution)
The **Strategic Import Dependency Score (SIDS)** is a novel composite metric developed for IndiaShield that measures India's vulnerability to supply chain disruptions from individual arms suppliers. It compiles concentration, single-source platforms, geopolitical alignment risks, and domestic indigenisation rates.

$$SIDS = \frac{IC}{100} \times SSR \times (1 - GSS) \times \frac{1}{DSC} \times 100$$

*   **Import Concentration (IC):** Percentage of total arms imports from the supplier.
*   **Single-Source Risk (SSR):** Weighted score reflecting lock-in levels (>60% in a platform category = 1.0, >40% = 0.6, else 0.2).
*   **Geopolitical Stability Score (GSS):** Measures political reliability (0.0 = high risk/sanctioned, 1.0 = stable ally).
*   **Domestic Substitution Capacity (DSC):** Speed of replacement (0.0 = irreplaceable, 1.0 = immediate local substitute).

### SIDS Risk Scale
*   **0-20:** Low Vulnerability (Green)
*   **21-40:** Moderate (Yellow)
*   **41-60:** High (Orange)
*   **61-80:** Critical (Red)
*   **81+:** Extreme (Dark Red)

## Data Sources
| Source | Description | URL |
| :--- | :--- | :--- |
| SIPRI Milex Database | Military Expenditure Database (constant USD) | [SIPRI Milex](https://sipri.org/databases/milex) |
| SIPRI Arms Transfers | Arms Transfers Database (recipient filter: India) | [SIPRI Arms Transfers](https://sipri.org/databases/armstransfers) |
| Union Budget of India | India's Ministry of Finance Defence budget details | [India Budget](https://www.indiabudget.gov.in/) |
| Yahoo Finance (NSE) | Daily closing prices for defence stocks (HAL, BEL, BEML, Mazagon Dock) | [Yahoo Finance](https://finance.yahoo.com/) |

## Manual Data Setup
To set up local databases manually:
1.  **SIPRI Military Expenditure:** Download the Excel dataset from the database URL, go to the sheet "Constant (2022) USD", filter rows for India, China, Pakistan, USA, Russia, France, UK, Israel, Saudi Arabia, Germany, Japan, and Australia, and save years 2000-2024 as `data/raw/sipri_milex.csv`.
2.  **SIPRI Arms Transfers:** Filter the SIPRI Arms Transfer database for Recipient=India, Years=2000-2024. Export details containing Year, Supplier, Recipient, Armament, and SIPRI_TIV, and save as `data/raw/sipri_arms_transfer.csv`.
3.  *Note:* The app has high-fidelity fallback libraries compiled into `modules/data_loader.py` and will run seamlessly even if these raw files are missing.

## Run Locally
To run the Streamlit app on your local system:
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Key Findings
*   **Budget Multiplier:** India's defence spend has grown **5.4×** since 2000 in constant dollars (from $15.9B to $86.1B).
*   **The Modernisation Paradox:** While total allocation grew, the share of Capital Expenditure (modernisation & acquisition) dropped from **38.3%** in 2015 to **28.9%** in 2024, showing manpower cost pressure.
*   **Critical Supplier Vulnerability:** Russia remains India's most critical supply-chain risk with a SIDS score of **72 (Critical)** due to active sanctions.
*   **Geopolitical Stock Hedge:** Defence stocks like HAL and BEL act as market hedges, generating average gains of **23%** in the 30 days following border escalations while the Nifty 50 declines.
*   **Indigenisation Gain:** Sourcing from domestic defence companies grew from **40%** to **65%** under Make in India between 2014 and 2024.
