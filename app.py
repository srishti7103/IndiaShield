import streamlit as st
import pandas as pd
from utils.styling import inject_custom_css
from modules.data_loader import load_military_expenditure, load_union_budget

# 1. Page Config (Must be the very first Streamlit command)
st.set_page_config(
    page_title="IndiaShield",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Inject Custom CSS
inject_custom_css()

# 3. Sidebar Setup
st.sidebar.markdown(
    """
    <div style="text-align: center; margin-bottom: 20px;">
        <h1 style="color: #C9A84C; font-size: 26px; font-weight: 800; margin: 0;">🛡️ IndiaShield</h1>
        <p style="color: #E2E8F0; font-size: 11px; font-weight: 500; text-transform: uppercase; letter-spacing: 0.08em; margin: 4px 0 0 0;">
            Strategic Defence Intelligence Platform
        </p>
    </div>
    <hr style="border: 1px solid #1A3A5C; margin: 0 0 20px 0;"/>
    """, 
    unsafe_allow_html=True
)

# Sidebar Navigation
navigation_options = [
    "🏠 Strategic Overview",
    "💰 Budget Anatomy",
    "⚔️ Regional Arms Race",
    "🔗 Arms Import Flow",
    "📦 Defence Exports",
        "📈 Market Intelligence"
]

page = st.sidebar.radio(
    "Navigation",
    options=navigation_options,
    label_visibility="collapsed"
)

st.sidebar.markdown('<hr style="border: 1px solid #1A3A5C; margin: 20px 0;"/>', unsafe_allow_html=True)

# 4. Context-Specific Sidebar Filters
# Global Year Range Slider (for Overview and Arms Race pages)
if page in ["🏠 Strategic Overview", "⚔️ Regional Arms Race"]:
    st.sidebar.subheader("📅 Filters")
    year_range = st.sidebar.slider(
        "Year Range:",
        min_value=2000,
        max_value=2024,
        value=(2000, 2024),
        step=1
    )
else:
    # Default range
    year_range = (2000, 2024)

# Country Selector (for Regional Arms Race page)
if page == "⚔️ Regional Arms Race":
    st.sidebar.subheader("🏳️ Compare Countries")
    # Tickers to query via constants list
    from utils.constants import COUNTRIES_ALL
    selected_countries = st.sidebar.multiselect(
        "Select Countries:",
        options=COUNTRIES_ALL,
        default=["India", "China", "Pakistan"]
    )
    if not selected_countries:
        selected_countries = ["India"]
else:
    selected_countries = ["India", "China", "Pakistan"]

# Budget Year Selector (for Budget Anatomy page)
if page == "💰 Budget Anatomy":
    st.sidebar.subheader("📅 Select FY Allocation")
    df_budget = load_union_budget()
    fy_options = list(df_budget['Year'].unique())
    selected_fy = st.sidebar.selectbox(
        "Financial Year:",
        options=fy_options,
        index=len(fy_options) - 1 # Default to latest (2024-25)
    )
else:
    selected_fy = "2024-25"


st.sidebar.markdown('<div style="height: 40px;"></div>', unsafe_allow_html=True)

# Bottom Sidebar Badges
st.sidebar.markdown(
    """
    <div style="background-color: #1A3A5C; border: 1px solid #C9A84C; border-radius: 8px; padding: 12px; font-size: 11px; text-align: center;">
        <span style="color: #C9A84C; font-weight: 700; text-transform: uppercase;">Data Sources Verified</span>
        <div style="color: #E2E8F0; margin-top: 6px; font-family: monospace; line-height: 1.4;">
            SIPRI Milex & Arms Database<br/>
            Ministry of Finance, Union Budget<br/>
            NSE Stock Equities via yfinance
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# 5. Page Rendering Router
if page == "🏠 Strategic Overview":
    from modules.overview import render_page
    render_page(year_range)
    
elif page == "📦 Defence Exports":
    from modules.exports_analysis import render_page
    render_page()

elif page == "💰 Budget Anatomy":
    from modules.budget_analysis import render_page
    render_page(selected_fy)
    
elif page == "⚔️ Regional Arms Race":
    from modules.arms_race import render_page
    render_page(year_range, selected_countries)
    
elif page == "🔗 Arms Import Flow":
    from modules.arms_import_flow import render_page
    render_page()
    
elif page == "📦 Defence Exports":
    from modules.exports_analysis import render_page
    render_page()

elif page == "📈 Market Intelligence":
    from modules.market_intelligence import render_page
    render_page()
