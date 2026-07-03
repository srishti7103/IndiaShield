import streamlit as st
import pandas as pd
from utils.styling import render_banner, render_kpi_card, render_gold_divider
from utils.charts import plot_india_spend_journey, plot_global_spend_map
from modules.data_loader import (
    load_military_expenditure, load_geopolitical_events, 
    load_union_budget, load_kpi_summary
)

def render_page(year_range):
    start_yr, end_yr = year_range
    
    # 1. Top Section - Banner
    render_banner(
        "India's Defence Ecosystem: A Data Intelligence Report",
        "25 Years of Strategic Spending, Arms Procurement & Regional Power Dynamics"
    )
    
    # Load required data
    df_spend = load_military_expenditure()
    df_events = load_geopolitical_events()
    df_budget = load_union_budget()
    kpi = load_kpi_summary()
    
    # 2. KPI Row - 4 Columns
    # Fetch values dynamically where possible
    spend_2024 = kpi['india_spend_2024']
    spend_2023 = df_spend[(df_spend['Country'] == 'India') & (df_spend['Year'] == 2023)]['Spend_USD_Bn'].values[0]
    delta_spend = ((spend_2024 - spend_2023) / spend_2023) * 100.0
    
    # Card 2: % of GDP
    gdp_pct_2024 = df_spend[(df_spend['Country'] == 'India') & (df_spend['Year'] == 2024)]['Spend_Pct_GDP'].values[0]
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        render_kpi_card(
            label="Defence Budget 2024",
            value=f"${spend_2024:.1f} Bn",
            delta=f"+{delta_spend:.1f}% vs 2023",
            delta_direction="up",
            footer=f"SIPRI, verified {kpi['verification_date']}"
        )
        
    with col2:
        render_kpi_card(
            label="% of GDP",
            value=f"{gdp_pct_2024:.1f}%",
            delta="Stable",
            delta_direction="neutral",
            footer=f"SIPRI, verified {kpi['verification_date']}"
        )
        
    with col3:
        render_kpi_card(
            label="Global Ranking",
            value=f"#{kpi['global_rank']}",
            footer=f"Behind USA, China, Russia, Germany · Verified {kpi['verification_date']}"
        )
        
    with col4:
        cap_pct = kpi['capital_share']
        rev_pct = kpi['revenue_share']
        render_kpi_card(
            label="Capital/Revenue Ratio",
            value=f"{cap_pct:.1f}% / {rev_pct:.1f}%",
            footer=f"{cap_pct:.1f}% goes to modernisation · Verified {kpi['verification_date']}"
        )
        
        
    render_gold_divider()
    
    # 3. Middle Section - 2 Columns (60% / 40%)
    mid_col1, mid_col2 = st.columns([3, 2])
    
    with mid_col1:
        # Animated line chart
        fig_journey = plot_india_spend_journey(df_spend, df_events, start_yr, end_yr)
        st.plotly_chart(fig_journey, use_container_width=True)
        
    with mid_col2:
        # Key Findings Card
        st.markdown(f"""
        <div class="insight-card">
            <div class="insight-title">Strategic Key Findings</div>
            <ul style="padding-left: 18px; margin: 0; color: #0D1B2A; font-size: 13px; line-height: 1.6;">
                <li style="margin-bottom: 8px;"><b>Spending Growth:</b> India's defence budget has expanded <b>5.4×</b> in constant terms over the last 24 years (from $15.9B to ${kpi['india_spend_2024']:.1f}B).</li>
                <li style="margin-bottom: 8px;"><b>The Capital Squeeze:</b> Share of budget for capital acquisitions (modernisation) fell from <b>38.3%</b> to <b>{kpi['capital_share']:.1f}%</b>, showing manpower and operation costs are squeezing weapons procurement.</li>
                <li style="margin-bottom: 8px;"><b>Russia Dependency:</b> Russia supplies <b>{kpi['russia_tiv_share']}%</b> of India's total arms import volume (SIPRI TIV, 2000–2024). Post-2022 sanctions present a critical risk for spare parts and lifecycle support of Russian-origin platforms.</li>
                <li style="margin-bottom: 8px;"><b>Stock Sensitivity:</b> Indian defence equities rally an average of <b>{kpi['post_escalation_return']:.1f}%</b> within 30 days of regional border escalations, yielding <b>+{kpi['post_escalation_alpha']:.1f}%</b> alpha.</li>
                <li style="margin-bottom: 8px;"><b>Indigenisation:</b> Domestic sourcing share of procurement rose from <b>40%</b> in 2014 to <b>65%</b> in 2024 under the 'Make in India' initiative.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
    render_gold_divider()
    
    # 4. Bottom Section - World Map
    fig_map = plot_global_spend_map(df_spend, end_yr)
    st.plotly_chart(fig_map, use_container_width=True)
