import streamlit as st
import pandas as pd
from utils.styling import render_banner, render_kpi_card, render_gold_divider
from utils.charts import plot_defence_exports_growth, plot_exports_import_ratio
from modules.data_loader import load_defence_exports, load_budget_data, load_kpi_summary


def render_page():
    render_banner(
        "Defence Exports — From Buyer to Seller",
        "Tracking India's shift from world's largest arms importer to emerging defence exporter — Source: Ministry of Defence"
    )

    df_exports = load_defence_exports()
    df_budget  = load_budget_data()

    if df_exports.empty:
        st.error("Defence exports data unavailable.")
        return

    render_gold_divider()

    kpi = load_kpi_summary()
    latest_exports = df_exports.iloc[-1]
    prev_exports = df_exports.iloc[-2]
    latest_val = latest_exports['Exports_INR_Cr']
    prev_val = prev_exports['Exports_INR_Cr']
    exports_delta = ((latest_val - prev_val) / prev_val) * 100.0

    # ── KPI row ───────────────────────────────────────────────────────────────
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        render_kpi_card(
            label="FY25 Exports",
            value=f"₹{latest_val:,.0f} Cr",
            delta=f"+{exports_delta:.1f}% vs {prev_exports['Year_Label']}",
            delta_direction="up",
            footer=f"MoD, verified {kpi['verification_date']}"
        )
    with col2:
        render_kpi_card(
            label="8-Year Growth",
            value=f"{kpi['defence_exports_growth']}×",
            delta=f"{df_exports.iloc[0]['Year_Label']} → {latest_exports['Year_Label']}",
            delta_direction="up",
            footer=f"MoD, verified {kpi['verification_date']}"
        )
    with col3:
        render_kpi_card(
            label="Export Target",
            value="₹50,000 Cr",
            delta="by FY29",
            delta_direction="up",
            footer=f"MoD Target, verified {kpi['verification_date']}"
        )
    with col4:
        render_kpi_card(
            label="Countries Served",
            value="100+",
            delta="as of FY25",
            delta_direction="neutral",
            footer=f"MoD, verified {kpi['verification_date']}"
        )

    render_gold_divider()

    # ── Main chart ────────────────────────────────────────────────────────────
    st.markdown("### 📈 Defence Exports Growth Trajectory (FY17–FY25)")
    st.caption(
        "Source: Ministry of Defence Annual Reports. "
        "FY25 figure is provisional. All INR values are nominal."
    )
    fig1 = plot_defence_exports_growth(df_exports)
    st.plotly_chart(fig1, use_container_width=True)

    render_gold_divider()

    # ── Ratio chart ───────────────────────────────────────────────────────────
    st.markdown("### ⚖️ Exports as % of Capital Expenditure")
    st.caption(
        "Comparing India's export revenue against its own capital defence spend. "
        "Rising ratio = India generating more export value relative to what it buys."
    )
    fig2 = plot_exports_import_ratio(df_exports, df_budget)
    st.plotly_chart(fig2, use_container_width=True)

    render_gold_divider()

    # ── Data table ────────────────────────────────────────────────────────────
    st.markdown("### 📋 Year-on-Year Export Data")
    display_df = df_exports[['Year_Label', 'Exports_INR_Cr', 'Exports_USD_Mn', 'Key_Event']].copy()
    display_df.columns = ['Financial Year', 'Exports (₹ Crore)', 'Exports (USD Mn)', 'Key Development']
    display_df['Exports (₹ Crore)'] = display_df['Exports (₹ Crore)'].apply(lambda x: f"₹{x:,.0f}")
    display_df['Exports (USD Mn)']  = display_df['Exports (USD Mn)'].apply(lambda x: f"${x:,.0f}")
    st.dataframe(display_df, use_container_width=True, hide_index=True)

    # Download button
    csv = df_exports.to_csv(index=False)
    st.download_button(
        label="⬇ Download Exports Data (CSV)",
        data=csv,
        file_name="india_defence_exports.csv",
        mime="text/csv"
    )

    render_gold_divider()

    st.markdown(
        f"""
        <div style="background-color:#1B4332; border-left:4px solid #C9A84C;
                    padding:16px 20px; border-radius:6px;">
            <span style="color:#C9A84C; font-weight:700; font-size:13px;">
                📌 Finding — The Buyer-to-Seller Transition
            </span>
            <p style="color:#E2E8F0; font-size:13px; margin:8px 0 0 0; line-height:1.6;">
                India's defence exports grew from <b>₹1,521 Crore in {df_exports.iloc[0]['Year_Label']}</b> to
                <b>₹{latest_val:,.0f} Crore in {latest_exports['Year_Label']}</b> — a <b>{kpi['defence_exports_growth']}× increase in 8 years</b>.
                Key export platforms include Brahmos supersonic cruise missiles
                (Philippines, ₹2,800 Cr contract), Dornier 228 maritime patrol aircraft,
                Advanced Towed Artillery Guns (ATAG), and electronic warfare systems from BEL.
                India now exports to <b>over 100 countries</b>, with a government target
                of ₹50,000 Crore by FY29. This is the clearest evidence that
                Make in India Defence is producing exportable capability —
                not just reducing imports.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
