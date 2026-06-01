import streamlit as st
from utils.constants import (
    NAVY_PRIMARY, NAVY_SECONDARY, GOLD_ACCENT, 
    FOREST_GREEN, THREAT_RED, WARM_GRAY, LIGHT_BG, CARD_BG, BORDER
)

def inject_custom_css():
    """Injects custom CSS to style the Streamlit app to military-strategic specifications."""
    css = f"""
    <style>
    /* Global Background and Fonts */
    .stApp {{
        background-color: {LIGHT_BG};
        font-family: 'Inter', 'Arial', sans-serif;
    }}
    
    /* Sidebar Styling */
    [data-testid="stSidebar"] {{
        background-color: {NAVY_PRIMARY} !important;
        color: #FFFFFF !important;
        border-right: 1px solid {NAVY_SECONDARY};
    }}
    [data-testid="stSidebar"] .stText, 
    [data-testid="stSidebar"] label, 
    [data-testid="stSidebar"] p, 
    [data-testid="stSidebar"] span,
    [data-testid="stSidebar"] h1,
    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3 {{
        color: #FFFFFF !important;
    }}
    [data-testid="stSidebar"] button {{
        color: #FFFFFF !important;
        background-color: {NAVY_SECONDARY} !important;
        border: 1px solid {GOLD_ACCENT} !important;
    }}
    [data-testid="stSidebar"] button:hover {{
        background-color: {GOLD_ACCENT} !important;
        color: {NAVY_PRIMARY} !important;
    }}
    
    /* Active Tab Gold Indicator */
    .stTabs [data-baseweb="tab-list"] {{
        border-bottom: 2px solid {BORDER} !important;
    }}
    .stTabs [data-baseweb="tab-list"] button {{
        color: {WARM_GRAY} !important;
        background-color: transparent !important;
        font-weight: 600 !important;
    }}
    .stTabs [data-baseweb="tab-list"] button[aria-selected="true"] {{
        color: {GOLD_ACCENT} !important;
        border-color: {GOLD_ACCENT} !important;
        border-bottom-width: 3px !important;
    }}
    
    /* DataFrame Styling overrides */
    div[data-testid="stDataFrame"] {{
        border: 1px solid {BORDER};
        border-radius: 8px;
        overflow: hidden;
    }}
    
    /* KPI Card styling class */
    .kpi-card {{
        background-color: {CARD_BG};
        border: 1px solid {BORDER};
        border-radius: 12px;
        padding: 20px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);
        transition: transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease;
        margin-bottom: 15px;
        height: 100%;
    }}
    .kpi-card:hover {{
        transform: translateY(-2px);
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.05), 0 4px 6px -2px rgba(0, 0, 0, 0.02);
        border-color: {GOLD_ACCENT};
    }}
    .kpi-label {{
        font-size: 11px;
        font-weight: 600;
        color: {WARM_GRAY};
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin-bottom: 8px;
    }}
    .kpi-value {{
        font-size: 28px;
        font-weight: 700;
        color: {NAVY_PRIMARY};
        line-height: 1.2;
    }}
    .kpi-delta-positive {{
        font-size: 13px;
        font-weight: 600;
        color: {FOREST_GREEN};
        margin-top: 4px;
    }}
    .kpi-delta-negative {{
        font-size: 13px;
        font-weight: 600;
        color: {THREAT_RED};
        margin-top: 4px;
    }}
    .kpi-delta-neutral {{
        font-size: 13px;
        font-weight: 600;
        color: {WARM_GRAY};
        margin-top: 4px;
    }}
    .kpi-footer {{
        font-size: 11px;
        color: {WARM_GRAY};
        margin-top: 8px;
    }}
    
    /* Divider */
    .gold-divider {{
        height: 2px;
        background: linear-gradient(90deg, {GOLD_ACCENT} 0%, rgba(201, 168, 76, 0.1) 100%);
        margin-top: 10px;
        margin-bottom: 25px;
        border: none;
    }}
    
    /* Page Banner */
    .banner-container {{
        background: linear-gradient(135deg, {NAVY_PRIMARY} 0%, {NAVY_SECONDARY} 100%);
        padding: 24px;
        border-radius: 12px;
        color: #FFFFFF;
        margin-bottom: 25px;
        border-left: 5px solid {GOLD_ACCENT};
    }}
    .banner-title {{
        font-size: 24px;
        font-weight: 700;
        color: {GOLD_ACCENT};
        margin: 0 0 4px 0;
    }}
    .banner-subtitle {{
        font-size: 14px;
        color: #E2E8F0;
        margin: 0;
        opacity: 0.9;
    }}

    /* Amber Callout Box */
    .amber-callout {{
        background-color: #FFFBEB;
        border-left: 4px solid #F59E0B;
        border-radius: 8px;
        padding: 16px;
        margin: 15px 0;
        color: #78350F;
    }}
    
    /* Red Callout Box */
    .red-callout {{
        background-color: #FEF2F2;
        border: 1px solid #FCA5A5;
        border-left: 4px solid {THREAT_RED};
        border-radius: 8px;
        padding: 16px;
        margin: 15px 0;
        color: #7F1D1D;
    }}
    
    /* General Insight Box (Styled Card) */
    .insight-card {{
        background-color: {CARD_BG};
        border: 1px solid {BORDER};
        border-radius: 8px;
        padding: 20px;
        margin-bottom: 15px;
        border-top: 3px solid {NAVY_SECONDARY};
    }}
    
    .insight-title {{
        font-size: 14px;
        font-weight: 700;
        color: {NAVY_PRIMARY};
        margin-top: 0;
        margin-bottom: 10px;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

def render_kpi_card(label, value, delta=None, delta_direction="up", footer=None):
    """Renders a custom styled KPI card using HTML/CSS inside Streamlit."""
    delta_html = ""
    if delta is not None:
        if delta_direction == "up":
            class_name = "kpi-delta-positive"
            prefix = "▲ "
        elif delta_direction == "down":
            class_name = "kpi-delta-negative"
            prefix = "▼ "
        else:
            class_name = "kpi-delta-neutral"
            prefix = ""
        delta_html = f'<div class="{class_name}">{prefix}{delta}</div>'
    
    footer_html = ""
    if footer is not None:
        footer_html = f'<div class="kpi-footer">{footer}</div>'
        
    card_html = f'<div class="kpi-card"><div class="kpi-label">{label}</div><div class="kpi-value">{value}</div>{delta_html}{footer_html}</div>'
    st.markdown(card_html, unsafe_allow_html=True)

def render_banner(title, subtitle):
    """Renders a full-width dark navy banner with gold left border."""
    banner_html = f'<div class="banner-container"><h1 class="banner-title">🛡️ {title}</h1><p class="banner-subtitle">{subtitle}</p></div>'
    st.markdown(banner_html, unsafe_allow_html=True)

def render_gold_divider():
    """Renders a custom gold gradient divider line."""
    st.markdown('<div class="gold-divider"></div>', unsafe_allow_html=True)

def render_amber_callout(text):
    """Renders an amber colored alert box for important insights."""
    callout_html = f'<div class="amber-callout">{text}</div>'
    st.markdown(callout_html, unsafe_allow_html=True)

def render_red_callout(text):
    """Renders a red colored warning box for critical alerts."""
    callout_html = f'<div class="red-callout">{text}</div>'
    st.markdown(callout_html, unsafe_allow_html=True)
