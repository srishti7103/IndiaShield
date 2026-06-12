import streamlit as st
from utils.styling import render_banner, render_gold_divider
from utils.charts import plot_arms_import_treemap, plot_arms_flow_sankey
from modules.data_loader import load_arms_transfers


def render_page():
    render_banner(
        "Arms Import Flow Analysis",
        "Visualising India's arms procurement footprint by supplier and weapon category — Source: SIPRI TIV Database"
    )

    df_transfers = load_arms_transfers()

    render_gold_divider()

    # Full-width Sankey
    st.markdown("### 📊 Arms Flow Pipeline — Supplier → Weapon Category")
    st.caption(
        "Flow width is proportional to SIPRI Trend Indicator Value (TIV). "
        "TIV measures military capability transferred, not contract cash value."
    )
    fig_sankey = plot_arms_flow_sankey(df_transfers)
    st.plotly_chart(fig_sankey, use_container_width=True)

    render_gold_divider()

    # Full-width Treemap
    st.markdown("### 🌳 Procurement Footprint — Supplier × Weapon Category")
    st.caption(
        "Size of each tile reflects total import volume (TIV). "
        "Colour identifies the supplier country."
    )
    fig_tree = plot_arms_import_treemap(df_transfers)
    st.plotly_chart(fig_tree, use_container_width=True)

    render_gold_divider()

    # Insight callout
    st.markdown(
        """
        <div style="background-color:#1A3A5C; border-left:4px solid #C9A84C;
                    padding:16px 20px; border-radius:6px; margin-top:8px;">
            <span style="color:#C9A84C; font-weight:700; font-size:13px;">
                📌 Key Finding — Supplier Concentration
            </span>
            <p style="color:#E2E8F0; font-size:13px; margin:8px 0 0 0; line-height:1.6;">
                Russia accounts for approximately <b>45%</b> of India's total arms import volume (TIV),
                dominating the Aircraft (70% of combat fleet) and Tanks/AFV (85% of armoured inventory)
                categories. France (11%) and the USA (9%) are the next largest suppliers,
                primarily covering Aircraft and Transport platforms respectively.
                Post-2022 sanctions on Russia have made this concentration a critical supply-chain risk
                for spare parts and lifecycle support of existing platforms.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
