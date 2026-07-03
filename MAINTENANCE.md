# IndiaShield Platform Maintenance and Synchronization Manual

This document details the architecture of the Single Source of Truth (SSoT) for IndiaShield KPIs and provides instructions for keeping the Tableau Public dashboard synchronized with the Streamlit data.

---

## 1. Single Source of Truth (`kpi_summary.json`)

All key metrics shown on the Streamlit dashboard KPI cards, Strategic Key Findings, and policy callouts are driven by a single JSON configuration file:
*   **Path**: [kpi_summary.json](file:///c:/Users/srrml/Desktop/PROJECTS/IndiaShield/data/processed/kpi_summary.json)
*   **Fields**:
    *   `global_rank`: The global ranking of India's defense expenditure (Germany is #4, India is #5 as of the 2024 SIPRI release).
    *   `india_spend_2024`: India's 2024 defense spend in USD Billions (Constant 2022 USD).
    *   `china_spend_2024`: China's 2024 defense spend in USD Billions.
    *   `china_gap`: The absolute budget gap between China and India ($318.0B - $86.1B = $231.9B).
    *   `capital_share`: Capital Expenditure as % of the total defense allocation (modernization share: 28.9%).
    *   `revenue_share`: Revenue Expenditure share (operations and personnel: 71.1%).
    *   `defence_exports_2024_inr`: Nominal defense exports in FY24 (₹21,083 Crore).
    *   `defence_exports_growth`: Growth multiplier of defense exports from FY17 to FY25 (14x).
    *   `russia_tiv_share`: Russia's share of India's total arms imports (63%).
    *   `post_escalation_return`: Reconciled 30-day post-escalation return average across defense stocks (17.2%).
    *   `post_escalation_alpha`: Mean outperformance (Alpha) over Nifty 50 Index (12.8%).
    *   `verification_date`: Data verification timestamp (e.g. `03 Jul 2026`).

---

## 2. Tableau Public Synchronization Steps

Tableau Public cannot dynamically query local Python files. To prevent data drift between the Streamlit app and the published Tableau workbook, follow this procedure before every publish:

1.  **Extract KPI Summary**:
    Ensure the values in [kpi_summary.json](file:///c:/Users/srrml/Desktop/PROJECTS/IndiaShield/data/processed/kpi_summary.json) are updated with any new SIPRI or Union Budget releases.
2.  **Export to Tableau Data Source**:
    Save/append these KPI summary values into the Excel/CSV sheets linked to the Tableau workbook.
3.  **Perform Diffs**:
    Verify the following visual cards inside the Tableau worksheets against `kpi_summary.json`:
    *   *Strategic Overview Sheet*: "Global Rank" card must match `global_rank` (#5) and "India Spend 2024" card must match `india_spend_2024` ($86.1 Bn).
    *   *Budget Anatomy Sheet*: "Capital Share" must match `capital_share` (28.9%).
    *   *Market Intelligence Sheet*: Text box return statistic must match `post_escalation_return` (17.2% average return).
4.  **Publish and Verify**:
    Publish the updated workbook to Tableau Public, open the live link, and confirm it aligns exactly with the Streamlit app KPIs.

---

## 3. Data Limits and Cutoffs

*   **Real Stock Data**: Stock price histories are pulled live or cached from `data/processed/stock_events.csv` via yfinance.
*   **Listing Cutoffs**: The data pipeline enforces exact listing dates for defense PSUs to prevent fake pre-IPO backfilled returns (e.g. Mazdock is excluded from event windows prior to 12 October 2020).
