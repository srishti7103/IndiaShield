import streamlit as st
import pandas as pd
from utils.styling import render_banner, render_kpi_card, render_gold_divider
from utils.charts import (
    plot_arms_race_spend, plot_arms_race_gdp, 
    plot_arms_race_cagr, plot_india_china_gap
)
from modules.data_loader import load_military_expenditure, load_kpi_summary

FLAGS = {
    "India": "🇮🇳",
    "China": "🇨🇳",
    "Pakistan": "🇵🇰",
    "United States": "🇺🇸",
    "Russia": "🇷🇺",
    "France": "🇫🇷",
    "United Kingdom": "🇬🇧",
    "Israel": "🇮🇱",
    "Saudi Arabia": "🇸🇦",
    "Germany": "🇩🇪",
    "Japan": "🇯🇵",
    "Australia": "🇦🇺"
}

def render_page(year_range, selected_countries):
    start_yr, end_yr = year_range
    
    # Dynamic Title based on selection
    vs_title = " vs ".join(selected_countries)
    render_banner(
        f"Regional Arms Race: {vs_title}",
        "25 Years of Strategic Competition in Numbers"
    )
    
    # Load spend data
    df_spend = load_military_expenditure()
    kpi = load_kpi_summary()
    
    # 1. Comparison KPI Cards
    st.write("### 📊 Selected Countries Profile (2024)")
    cols = st.columns(len(selected_countries))
    
    for i, country in enumerate(selected_countries):
        df_c = df_spend[df_spend['Country'] == country]
        # Latest data for 2024
        row_2024 = df_c[df_c['Year'] == 2024]
        row_2023 = df_c[df_c['Year'] == 2023]
        
        if not row_2024.empty:
            budget = row_2024.iloc[0]['Spend_USD_Bn']
            gdp_pct = row_2024.iloc[0]['Spend_Pct_GDP']
            
            if not row_2023.empty:
                prev_budget = row_2023.iloc[0]['Spend_USD_Bn']
                yoy = ((budget - prev_budget) / prev_budget) * 100.0
                yoy_text = f"{yoy:+.1f}% YoY"
                direction = "up" if yoy > 0 else "down"
            else:
                yoy_text = "N/A"
                direction = "neutral"
                
            flag = FLAGS.get(country, "🌐")
            with cols[i]:
                render_kpi_card(
                    label=f"{flag} {country}",
                    value=f"${budget:.1f} Bn",
                    delta=f"{gdp_pct:.1f}% of GDP",
                    delta_direction="neutral",
                    footer=f"{yoy_text} · Verified {kpi['verification_date']}"
                )
                
    render_gold_divider()
    
    # 2. Spend Over Time (with play animation if possible, otherwise interactive)
    # Plotly figures in Streamlit are rendered interactively. We will provide a clean multi-line plot.
    fig_spend = plot_arms_race_spend(df_spend, selected_countries, start_yr, end_yr)
    st.plotly_chart(fig_spend, use_container_width=True)
    
    render_gold_divider()
    
    # 3. Spend % GDP Chart
    fig_gdp = plot_arms_race_gdp(df_spend, selected_countries, start_yr, end_yr)
    st.plotly_chart(fig_gdp, use_container_width=True)
    
    st.markdown("""
    <div style="font-size: 13px; color: #6C757D; margin-top: -10px; margin-bottom: 20px;">
        💡 <i>Insight: Pakistan spends a significantly higher portion of its GDP on defense compared to India and China, reflecting a heavy relative defence burden despite its smaller absolute budget.</i>
    </div>
    """, unsafe_allow_html=True)
    
    render_gold_divider()
    
    # 4. Bottom Row (CAGR & Gap)
    col1, col2 = st.columns(2)
    
    with col1:
        fig_cagr = plot_arms_race_cagr(df_spend, selected_countries)
        st.plotly_chart(fig_cagr, use_container_width=True)
        
    with col2:
        # Gap chart is only relevant for India vs China
        fig_gap = plot_india_china_gap(df_spend)
        st.plotly_chart(fig_gap, use_container_width=True)
        
    render_gold_divider()
    
    # 5. Strategic Insight Box
    st.markdown("""
    <div class="insight-card" style="border-left: 4px solid #C1121F;">
        <div class="insight-title" style="color: #C1121F;">Strategic Insight: The China Gap</div>
        <p style="font-size: 13px; line-height: 1.6; margin: 0; color: #0D1B2A;">
            In 2000, China spent approximately 2× India's defence budget. By 2024, that gap has grown to <b>3.7×</b>. 
            Even as India's budget grew a substantial 5× over this period, China's aggressive modernization program expanded 
            its budget by <b>9.6×</b> in absolute constant terms, creating a significant strategic and capabilities gap.
        </p>
    </div>
    """, unsafe_allow_html=True)
