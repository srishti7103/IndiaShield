import streamlit as st
from utils.styling import render_banner, render_gold_divider
from utils.charts import plot_arms_import_treemap, plot_arms_flow_sankey
from modules.data_loader import load_arms_transfers, load_kpi_summary

def render_page():
    render_banner("Arms Import Flow Analysis",
        "India's arms procurement footprint by supplier and weapon category — Source: SIPRI Arms Transfers Database")
    df_transfers = load_arms_transfers()
    kpi = load_kpi_summary()
    render_gold_divider()
    st.markdown("### 📊 Arms Flow Pipeline — Supplier → Weapon Category")
    st.caption("Flow width is proportional to SIPRI Trend Indicator Value (TIV). Source: SIPRI Arms Transfers Database, 2000–2024.")
    st.plotly_chart(plot_arms_flow_sankey(df_transfers), use_container_width=True)
    render_gold_divider()
    st.markdown("### 🌳 Procurement Footprint — Supplier × Weapon Category")
    st.caption("Tile size = total TIV volume. Colour = supplier country. Source: SIPRI Arms Transfers Database.")
    st.plotly_chart(plot_arms_import_treemap(df_transfers), use_container_width=True)
    render_gold_divider()
    st.markdown(f"""
        <div style="background-color:#1A3A5C;border-left:4px solid #C9A84C;padding:16px 20px;border-radius:6px;">
        <span style="color:#C9A84C;font-weight:700;font-size:13px;">📌 Finding — Supplier Concentration</span>
        <p style="color:#E2E8F0;font-size:13px;margin:8px 0 0 0;line-height:1.6;">
        Russia accounts for <b>{kpi['russia_tiv_share']}%</b> of India's total arms import volume (SIPRI TIV, 2000–2024) —
        the highest supplier concentration of any major military power.
        France (9.5%), Israel (8.6%), and USA (8.1%) are the next largest suppliers.
        Post-2022 international sanctions have placed spare-parts supply and lifecycle support
        for Russian-origin platforms under direct pressure.
        <br><br><i>Source: SIPRI Arms Transfers Database · Verified {kpi['verification_date']}</i>
        </p></div>""", unsafe_allow_html=True)
