import streamlit as st
import pandas as pd
from utils.styling import render_banner, render_kpi_card, render_gold_divider, render_amber_callout
from utils.charts import (
    plot_budget_stacked_area, plot_budget_donut, 
    plot_capital_utilisation, plot_capital_pct_trend
)
from modules.data_loader import load_union_budget, load_kpi_summary

def render_page(selected_year):
    # Top Banner
    render_banner(
        "Budget Anatomy: Where Does India's Defence Money Go?",
        "Capital vs. Revenue Expenditure Analysis (2015-2024)"
    )
    
    # Load budget data
    df_budget = load_union_budget()
    kpi = load_kpi_summary()
    
    # Find matching row for KPIs (selected_year is financial year format like '2024-25')
    row = df_budget[df_budget['Year'] == selected_year]
    if row.empty:
        row = df_budget.iloc[-1:] # Fallback to latest
        
    r = row.iloc[0]
    total_defence = r['Total_Defence']
    mod_spend = r['Modernisation']
    mod_pct = (mod_spend / total_defence) * 100.0
    drdo = r['DRDO']
    
    # Calculate DRDO YoY
    idx = df_budget[df_budget['Year'] == r['Year']].index[0]
    if idx > 0:
        prev_drdo = df_budget.loc[idx - 1, 'DRDO']
        drdo_yoy = ((drdo - prev_drdo) / prev_drdo) * 100.0
        drdo_delta = f"+{drdo_yoy:.1f}% YoY"
    else:
        drdo_delta = "N/A"
        
    # 1. KPI Row - 3 Columns
    col1, col2, col3 = st.columns(3)
    
    with col1:
        render_kpi_card(
            label=f"FY {selected_year} Total Budget",
            value=f"₹{total_defence:,.0f} Cr",
            footer=f"MoF, verified {kpi['verification_date']}"
        )
        
    with col2:
        render_kpi_card(
            label="Modernisation Spend",
            value=f"₹{mod_spend:,.0f} Cr",
            footer=f"{mod_pct:.1f}% of budget · Verified {kpi['verification_date']}"
        )
        
    with col3:
        render_kpi_card(
            label="DRDO Allocation (R&D)",
            value=f"₹{drdo:,.0f} Cr",
            delta=drdo_delta,
            delta_direction="up" if idx > 0 and drdo_yoy > 0 else "neutral",
            footer=f"MoF, verified {kpi['verification_date']}"
        )
        
    render_gold_divider()
    
    # 2. Main Stacked Area Chart (Full Width)
    fig_stacked = plot_budget_stacked_area(df_budget)
    st.plotly_chart(fig_stacked, use_container_width=True)
    
    render_gold_divider()
    
    # 3. Middle Row - 2 Columns (Donut Chart & Bar Chart)
    mid_col1, mid_col2 = st.columns(2)
    
    with mid_col1:
        fig_donut = plot_budget_donut(df_budget, selected_year)
        st.plotly_chart(fig_donut, use_container_width=True)
        
    with mid_col2:
        fig_util = plot_capital_utilisation(df_budget)
        st.plotly_chart(fig_util, use_container_width=True)
        
    render_gold_divider()
    
    # 4. Bottom Section - Insight Box and Line Chart
    render_amber_callout(
        f"⚠️ <b>The Modernisation Paradox:</b> India's total defence budget has grown 5× since 2015, "
        f"but the share going to actual weapons and platform acquisition (Capital Expenditure) has "
        f"FALLEN from 38.3% to {kpi['capital_share']:.1f}%. Of every ₹100 spent on defence, only ₹{kpi['capital_share']:.0f} buys new capability."
    )
    
    fig_trend = plot_capital_pct_trend(df_budget)
    st.plotly_chart(fig_trend, use_container_width=True)
