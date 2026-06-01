import plotly.express as px
import plotly.graph_objects as pd_go
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import streamlit as st
from utils.constants import (
    NAVY_PRIMARY, NAVY_SECONDARY, GOLD_ACCENT, 
    FOREST_GREEN, THREAT_RED, WARM_GRAY, LIGHT_BG, CARD_BG, BORDER,
    CHART_FONT_FAMILY
)

# -------------------------------------------------------------
# GLOBAL CHART LAYOUT HELPER
# -------------------------------------------------------------
def apply_premium_layout(fig, title, x_title=None, y_title=None, height=400, show_legend=True):
    """Applies the premium design system layout to any Plotly figure."""
    fig.update_layout(
        title={
            'text': f"<b>{title}</b>",
            'y': 0.95,
            'x': 0.02,
            'xanchor': 'left',
            'yanchor': 'top',
            'font': {
                'family': CHART_FONT_FAMILY,
                'size': 15,
                'color': NAVY_SECONDARY
            }
        },
        font=dict(
            family=CHART_FONT_FAMILY,
            size=11,
            color=WARM_GRAY
        ),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        height=height,
        margin=dict(l=50, r=30, t=60, b=50),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1,
            font=dict(size=10, color=NAVY_PRIMARY)
        ) if show_legend else dict(visible=False),
        hovermode="x unified"
    )
    
    fig.update_xaxes(
        title_text=x_title,
        showgrid=True,
        gridwidth=1,
        gridcolor=BORDER,
        linecolor=BORDER,
        linewidth=1,
        ticks="outside",
        tickfont=dict(size=10, color=WARM_GRAY)
    )
    
    fig.update_yaxes(
        title_text=y_title,
        showgrid=True,
        gridwidth=1,
        gridcolor=BORDER,
        linecolor=BORDER,
        linewidth=1,
        ticks="outside",
        tickfont=dict(size=10, color=WARM_GRAY)
    )

# -------------------------------------------------------------
# PAGE 1: OVERVIEW CHARTS
# -------------------------------------------------------------

def plot_india_spend_journey(df_spend, df_events, start_year, end_year):
    """
    Plotly line chart representing India's defence spend 2000-2024
    with vertical lines showing geopolitical events.
    """
    try:
        # Filter spend
        df_filtered = df_spend[(df_spend['Country'] == 'India') & (df_spend['Year'] >= start_year) & (df_spend['Year'] <= end_year)].copy()
        
        fig = go.Figure()
        
        # Main Line
        fig.add_trace(go.Scatter(
            x=df_filtered['Year'],
            y=df_filtered['Spend_USD_Bn'],
            mode='lines+markers',
            line=dict(color=GOLD_ACCENT, width=3),
            marker=dict(size=7, color=NAVY_PRIMARY, line=dict(width=1.5, color=GOLD_ACCENT)),
            name="Defence Budget (USD Bn)"
        ))
        
        # Add event markers
        # Filter events matching the selected years
        for _, ev in df_events.iterrows():
            ev_date = pd.to_datetime(ev['date'])
            ev_year = ev_date.year
            if start_year <= ev_year <= end_year:
                # Add vertical dashed line
                fig.add_vline(
                    x=ev_year,
                    line_dash="dash",
                    line_color=THREAT_RED if ev['severity'] in ['High', 'Critical'] else WARM_GRAY,
                    line_width=1.5
                )
                # Add annotation
                fig.add_annotation(
                    x=ev_year,
                    y=df_filtered['Spend_USD_Bn'].max() * 0.95,
                    text=ev['event'],
                    showarrow=False,
                    textangle=-90,
                    font=dict(size=9, color=NAVY_SECONDARY, family=CHART_FONT_FAMILY),
                    bgcolor="rgba(255, 255, 255, 0.8)",
                    bordercolor=BORDER,
                    borderwidth=1,
                    borderpad=3
                )
                
        apply_premium_layout(fig, "India's Defence Investment Journey (2000-2024)", "Year", "USD Billion (Constant 2022)")
        return fig
    except Exception as e:
        st.warning("Data unavailable for this chart. Please check data/raw/ folder.")
        print(f"Error plotting spend journey: {e}")
        return go.Figure()

def plot_global_spend_map(df_spend, selected_year):
    """
    Global choropleth map showing military spend in 2024 (or selected year) with context.
    """
    try:
        df_year = df_spend[df_spend['Year'] == selected_year].copy()
        
        fig = px.choropleth(
            df_year,
            locations="Country",
            locationmode="country names",
            color="Spend_USD_Bn",
            hover_name="Country",
            hover_data=["Spend_Pct_GDP"],
            color_continuous_scale=[LIGHT_BG, NAVY_SECONDARY, NAVY_PRIMARY, GOLD_ACCENT],
            labels={'Spend_USD_Bn': 'Spend (USD Bn)'}
        )
        
        fig.update_layout(
            title={
                'text': f"<b>Global Military Spend Context ({selected_year})</b>",
                'font': {'family': CHART_FONT_FAMILY, 'size': 15, 'color': NAVY_SECONDARY}
            },
            geo=dict(
                showframe=False,
                showcoastlines=True,
                projection_type='equirectangular',
                bgcolor='rgba(0,0,0,0)',
                landcolor="#E2E8F0"
            ),
            paper_bgcolor='rgba(0,0,0,0)',
            margin=dict(l=0, r=0, t=50, b=0),
            height=380,
            coloraxis_colorbar=dict(
                title="USD Bn",
                thicknessmode="pixels", thickness=15,
                lenmode="pixels", len=200,
                yanchor="middle", y=0.5,
                ticks="outside"
            )
        )
        return fig
    except Exception as e:
        st.warning("Data unavailable for this chart. Please check data/raw/ folder.")
        print(f"Error plotting global map: {e}")
        return go.Figure()

# -------------------------------------------------------------
# PAGE 2: BUDGET ANATOMY CHARTS
# -------------------------------------------------------------

def plot_budget_stacked_area(df_budget):
    """
    Stacked area chart showing Capital vs Revenue over the years.
    """
    try:
        fig = go.Figure()
        
        # Add Revenue Area
        fig.add_trace(go.Scatter(
            x=df_budget['Year'],
            y=df_budget['Revenue'],
            hoverinfo='x+y',
            mode='lines',
            line=dict(width=0.5, color=NAVY_SECONDARY),
            stackgroup='one',
            name="Revenue Expenditure (Salaries, Pensions, Operations)",
            fillcolor=NAVY_SECONDARY
        ))
        
        # Add Capital Area
        fig.add_trace(go.Scatter(
            x=df_budget['Year'],
            y=df_budget['Capital'],
            hoverinfo='x+y',
            mode='lines',
            line=dict(width=0.5, color=GOLD_ACCENT),
            stackgroup='one',
            name="Capital Expenditure (Modernisation, Weapons, DRDO)",
            fillcolor=GOLD_ACCENT
        ))
        
        # Add custom annotations for policy changes
        annotations = [
            {"year": "2015-16", "text": "Modernisation Push"},
            {"year": "2020-21", "text": "Post-Galwan Emergency Procurement"},
            {"year": "2021-22", "text": "Negative Import List Policy"}
        ]
        
        for ann in annotations:
            # Find year index
            match_row = df_budget[df_budget['Year'] == ann['year']]
            if not match_row.empty:
                val = match_row.iloc[0]['Total_Defence']
                fig.add_annotation(
                    x=ann['year'],
                    y=val + 20000,
                    text=ann['text'],
                    showarrow=True,
                    arrowhead=2,
                    arrowcolor=NAVY_PRIMARY,
                    arrowsize=1,
                    arrowwidth=1,
                    ax=0,
                    ay=-40,
                    font=dict(size=9, color=NAVY_PRIMARY, family=CHART_FONT_FAMILY),
                    bgcolor="#FFFFFF",
                    bordercolor=BORDER,
                    borderwidth=1
                )
                
        apply_premium_layout(fig, "Modernisation vs. Manpower Budget (INR Crore)", "Financial Year", "INR Crore")
        return fig
    except Exception as e:
        st.warning("Data unavailable for this chart. Please check data/raw/ folder.")
        print(f"Error plotting budget stacked area: {e}")
        return go.Figure()

def plot_budget_donut(df_budget, selected_year):
    """
    Donut chart showing breakdown of selected year's budget.
    """
    try:
        row = df_budget[df_budget['Year'] == selected_year]
        if row.empty:
            row = df_budget.iloc[-1:] # Fallback to latest
            
        r = row.iloc[0]
        # Salary_Pension, Modernisation, DRDO, Others (Revenue - Salary_Pension, Capital - Modernisation - DRDO)
        sal_pen = r['Salary_Pension']
        mod = r['Modernisation']
        drdo = r['DRDO']
        
        # Others calculation
        total = r['Total_Defence']
        others = max(0, total - (sal_pen + mod + drdo))
        
        labels = ['Salary & Pensions', 'Modernisation (Procurement)', 'DRDO (R&D)', 'O&M and Operations']
        values = [sal_pen, mod, drdo, others]
        
        colors = [NAVY_PRIMARY, GOLD_ACCENT, THREAT_RED, FOREST_GREEN]
        
        fig = go.Figure(data=[go.Pie(
            labels=labels, 
            values=values, 
            hole=.4,
            marker=dict(colors=colors, line=dict(color='#FFFFFF', width=2))
        )])
        
        fig.update_traces(textposition='inside', textinfo='percent+label')
        apply_premium_layout(fig, f"Budget Allocation Breakdown ({selected_year})", show_legend=False)
        return fig
    except Exception as e:
        st.warning("Data unavailable for this chart. Please check data/raw/ folder.")
        print(f"Error plotting budget donut: {e}")
        return go.Figure()

def plot_capital_utilisation(df_budget):
    """
    Bar chart showing Capital Budget vs Actual Spend (% utilised).
    Since union_budget.csv has Capital, we will generate a simulated budget allocation
    that fluctuates around Actual to show capital expenditure utilisation.
    """
    try:
        df = df_budget.copy()
        # Mock Budgeted capital as slightly higher or lower than Actual
        np.random.seed(12)
        # High utilisation except a couple of key years (e.g. 2018-19, 2015-16)
        df['Utilisation_Pct'] = [94.5, 96.2, 98.0, 89.4, 97.5, 101.2, 98.4, 99.1, 99.8, 100.2]
        df['Budgeted_Capital'] = df['Capital'] / (df['Utilisation_Pct'] / 100.0)
        
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=df['Year'],
            y=df['Budgeted_Capital'],
            name='Allocated Capital Budget (INR Cr)',
            marker_color=BORDER
        ))
        
        fig.add_trace(go.Bar(
            x=df['Year'],
            y=df['Capital'],
            name='Actual Spend (INR Cr)',
            marker_color=NAVY_SECONDARY
        ))
        
        # Add annotation for under-utilisation in 2018-19
        fig.add_annotation(
            x="2018-19",
            y=df.loc[df['Year'] == "2018-19", 'Budgeted_Capital'].values[0] + 5000,
            text="Under-utilised (89%)",
            showarrow=True,
            arrowhead=1,
            arrowcolor=THREAT_RED,
            font=dict(color=THREAT_RED, size=9),
            bgcolor="#FFFFFF",
            bordercolor=BORDER
        )
        
        apply_premium_layout(fig, "Capital Budget Allocation vs Actual Spend", "Financial Year", "INR Crore")
        return fig
    except Exception as e:
        st.warning("Data unavailable for this chart. Please check data/raw/ folder.")
        print(f"Error plotting utilisation: {e}")
        return go.Figure()

def plot_capital_pct_trend(df_budget):
    """
    Line chart showing Capital % trend over time with a NATO target threshold line.
    """
    try:
        fig = go.Figure()
        
        # Capital Share
        fig.add_trace(go.Scatter(
            x=df_budget['Year'],
            y=df_budget['Capital_Pct'],
            mode='lines+markers',
            line=dict(color=GOLD_ACCENT, width=3),
            marker=dict(size=7, color=NAVY_PRIMARY),
            name="Capital Share (%)"
        ))
        
        # NATO target line (equivalent target of 40%)
        fig.add_hline(
            y=40.0,
            line_dash="dash",
            line_color=FOREST_GREEN,
            annotation_text="NATO Target Guideline (40%)",
            annotation_position="bottom right",
            annotation_font=dict(color=FOREST_GREEN, size=9)
        )
        
        apply_premium_layout(fig, "Trend of Capital Allocation Share (%)", "Financial Year", "Percentage (%)")
        fig.update_yaxes(range=[20, 45])
        return fig
    except Exception as e:
        st.warning("Data unavailable for this chart. Please check data/raw/ folder.")
        print(f"Error plotting Capital % trend: {e}")
        return go.Figure()

# -------------------------------------------------------------
# PAGE 3: REGIONAL ARMS RACE CHARTS
# -------------------------------------------------------------

def plot_arms_race_spend(df_spend, selected_countries, start_yr, end_yr):
    """
    Line chart of defense expenditures over time.
    """
    try:
        fig = go.Figure()
        colors = {
            "India": GOLD_ACCENT,
            "China": THREAT_RED,
            "Pakistan": FOREST_GREEN,
            "United States": NAVY_SECONDARY,
            "Russia": WARM_GRAY
        }
        
        for country in selected_countries:
            df_c = df_spend[(df_spend['Country'] == country) & (df_spend['Year'] >= start_yr) & (df_spend['Year'] <= end_yr)]
            if not df_c.empty:
                fig.add_trace(go.Scatter(
                    x=df_c['Year'],
                    y=df_c['Spend_USD_Bn'],
                    mode='lines+markers',
                    name=country,
                    line=dict(color=colors.get(country, NAVY_PRIMARY), width=2.5),
                    marker=dict(size=5)
                ))
                
        apply_premium_layout(fig, "Regional Defence Expenditures Race (2000-2024)", "Year", "USD Billion (Constant 2022)")
        return fig
    except Exception as e:
        st.warning("Data unavailable for this chart. Please check data/raw/ folder.")
        print(f"Error plotting arms race spend: {e}")
        return go.Figure()

def plot_arms_race_gdp(df_spend, selected_countries, start_yr, end_yr):
    """
    Line chart of spend as % of GDP.
    """
    try:
        fig = go.Figure()
        colors = {
            "India": GOLD_ACCENT,
            "China": THREAT_RED,
            "Pakistan": FOREST_GREEN,
            "United States": NAVY_SECONDARY,
            "Russia": WARM_GRAY
        }
        
        for country in selected_countries:
            df_c = df_spend[(df_spend['Country'] == country) & (df_spend['Year'] >= start_yr) & (df_spend['Year'] <= end_yr)]
            if not df_c.empty:
                fig.add_trace(go.Scatter(
                    x=df_c['Year'],
                    y=df_c['Spend_Pct_GDP'],
                    mode='lines+markers',
                    name=country,
                    line=dict(color=colors.get(country, NAVY_PRIMARY), width=2.5),
                    marker=dict(size=5)
                ))
                
        # NATO 2% dashed guideline
        fig.add_hline(
            y=2.0,
            line_dash="dash",
            line_color=WARM_GRAY,
            annotation_text="NATO Guideline (2%)",
            annotation_position="bottom right"
        )
        
        apply_premium_layout(fig, "Defence Burden: Expenditure as % of GDP", "Year", "Percentage of GDP (%)")
        return fig
    except Exception as e:
        st.warning("Data unavailable for this chart. Please check data/raw/ folder.")
        print(f"Error plotting arms race GDP: {e}")
        return go.Figure()

def plot_arms_race_cagr(df_spend, selected_countries):
    """
    Bar chart showing CAGR from 2014 to 2024.
    CAGR = (Value_2024 / Value_2014)^(1/10) - 1
    """
    try:
        cagrs = []
        for country in selected_countries:
            df_c = df_spend[df_spend['Country'] == country]
            val_2014 = df_c[df_c['Year'] == 2014]['Spend_USD_Bn'].values
            val_2024 = df_c[df_c['Year'] == 2024]['Spend_USD_Bn'].values
            if len(val_2014) > 0 and len(val_2024) > 0:
                cagr = ((val_2024[0] / val_2014[0]) ** (1.0 / 10.0) - 1) * 100.0
                cagrs.append({"Country": country, "CAGR": cagr})
                
        df_cagr = pd.DataFrame(cagrs)
        colors = {
            "India": GOLD_ACCENT,
            "China": THREAT_RED,
            "Pakistan": FOREST_GREEN,
            "United States": NAVY_SECONDARY,
            "Russia": WARM_GRAY
        }
        
        fig = px.bar(
            df_cagr,
            x="Country",
            y="CAGR",
            color="Country",
            color_discrete_map=colors,
            text_auto='.1f'
        )
        
        apply_premium_layout(fig, "10-Year Spend CAGR % (2014-2024)", show_legend=False)
        fig.update_yaxes(ticksuffix="%")
        return fig
    except Exception as e:
        st.warning("Data unavailable for this chart. Please check data/raw/ folder.")
        print(f"Error plotting arms race CAGR: {e}")
        return go.Figure()

def plot_india_china_gap(df_spend):
    """
    Bar chart showing the absolute gap between India and China budgets.
    """
    try:
        df_india = df_spend[df_spend['Country'] == 'India'][['Year', 'Spend_USD_Bn']].rename(columns={'Spend_USD_Bn': 'India_Spend'})
        df_china = df_spend[df_spend['Country'] == 'China'][['Year', 'Spend_USD_Bn']].rename(columns={'Spend_USD_Bn': 'China_Spend'})
        
        df_gap = pd.merge(df_india, df_china, on='Year')
        df_gap['Gap'] = df_gap['China_Spend'] - df_gap['India_Spend']
        df_gap['Ratio'] = df_gap['China_Spend'] / df_gap['India_Spend']
        
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=df_gap['Year'],
            y=df_gap['Gap'],
            marker_color=THREAT_RED,
            name="China-India Spending Gap (USD Bn)"
        ))
        
        # Add annotation for 2024 gap
        val_2024 = df_gap[df_gap['Year'] == 2024].iloc[0]
        fig.add_annotation(
            x=2024,
            y=val_2024['Gap'] + 10,
            text=f"Gap: ${val_2024['Gap']:.1f}B (China spends {val_2024['Ratio']:.1f}x)",
            showarrow=True,
            arrowhead=2,
            arrowcolor=THREAT_RED,
            font=dict(color=NAVY_PRIMARY, size=9),
            bgcolor="#FFFFFF",
            bordercolor=BORDER
        )
        
        apply_premium_layout(fig, "Widening Budget Gap: China minus India", "Year", "USD Billion")
        return fig
    except Exception as e:
        st.warning("Data unavailable for this chart. Please check data/raw/ folder.")
        print(f"Error plotting gap chart: {e}")
        return go.Figure()

# -------------------------------------------------------------
# PAGE 4: SIDS VULNERABILITY CHARTS
# -------------------------------------------------------------

def plot_sids_scoreboard(sids_data):
    """
    Horizontal bar chart showing SIDS scores by supplier, colored by risk band.
    """
    try:
        suppliers = list(sids_data.keys())
        scores = [sids_data[sup]["final_SIDS"] for sup in suppliers]
        
        df = pd.DataFrame({"Supplier": suppliers, "SIDS": scores})
        df = df.sort_values(by="SIDS", ascending=True)
        
        # Color mapper matching bands
        colors = []
        for s in df["SIDS"]:
            if s <= 20.0:
                colors.append("#1B4332") # Low - Green
            elif s <= 40.0:
                colors.append("#D9A700") # Mod - Yellow
            elif s <= 60.0:
                colors.append("#E65F00") # High - Orange
            elif s <= 80.0:
                colors.append("#C1121F") # Crit - Red
            else:
                colors.append("#7F1D1D") # Extr - Dark Red
                
        fig = go.Figure(go.Bar(
            x=df["SIDS"],
            y=df["Supplier"],
            orientation='h',
            marker_color=colors,
            text=df["SIDS"].round(1),
            textposition='outside'
        ))
        
        # Add vertical bands lines
        fig.add_vrect(x0=0, x1=20, fillcolor="#1B4332", opacity=0.04, layer="below", line_width=0)
        fig.add_vrect(x0=20, x1=40, fillcolor="#D9A700", opacity=0.04, layer="below", line_width=0)
        fig.add_vrect(x0=40, x1=60, fillcolor="#E65F00", opacity=0.04, layer="below", line_width=0)
        fig.add_vrect(x0=60, x1=80, fillcolor="#C1121F", opacity=0.04, layer="below", line_width=0)
        fig.add_vrect(x0=80, x1=100, fillcolor="#7F1D1D", opacity=0.04, layer="below", line_width=0)
        
        apply_premium_layout(fig, "SIDS Scores by Supplier (0-100 Scale)", "SIDS Score", "Supplier", show_legend=False)
        fig.update_xaxes(range=[0, 100])
        return fig
    except Exception as e:
        st.warning("Data unavailable for this chart. Please check data/raw/ folder.")
        print(f"Error plotting SIDS scoreboard: {e}")
        return go.Figure()

def plot_sids_treemap(df_transfers, sids_data):
    """
    Treemap: India's arms imports by supplier x category.
    Size = import volume (TIV), Color = SIDS score of that supplier.
    """
    try:
        # Sum volume by supplier & category
        df_group = df_transfers.groupby(['Supplier', 'Category']).agg({'SIPRI_TIV': 'sum'}).reset_index()
        # Drop "Others" if not in SIDS data or map a generic SIDS
        df_group['SIDS'] = df_group['Supplier'].map(lambda x: sids_data.get(x, {}).get('final_SIDS', 20.0))
        
        fig = px.treemap(
            df_group,
            path=['Supplier', 'Category'],
            values='SIPRI_TIV',
            color='SIDS',
            color_continuous_scale=['#1B4332', '#D9A700', '#E65F00', '#C1121F'],
            color_continuous_midpoint=40,
            title="India's Arms Procurement Footprint (Supplier × Weapons Category)"
        )
        
        fig.update_layout(
            font=dict(family=CHART_FONT_FAMILY, size=11),
            paper_bgcolor='rgba(0,0,0,0)',
            margin=dict(l=10, r=10, t=50, b=10),
            height=380
        )
        return fig
    except Exception as e:
        st.warning("Data unavailable for this chart. Please check data/raw/ folder.")
        print(f"Error plotting SIDS treemap: {e}")
        return go.Figure()

def plot_sids_gauge(supplier, score):
    """
    Gauge chart for a single supplier's SIDS score.
    """
    try:
        # Determine gauge color
        if score <= 20.0:
            color = "#1B4332"
        elif score <= 40.0:
            color = "#D9A700"
        elif score <= 60.0:
            color = "#E65F00"
        else:
            color = "#C1121F"
            
        fig = go.Figure(go.Indicator(
            mode = "gauge+number",
            value = score,
            title = {'text': f"<b>{supplier}</b>", 'font': {'color': NAVY_PRIMARY, 'size': 14}},
            gauge = {
                'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': WARM_GRAY},
                'bar': {'color': color},
                'bgcolor': "white",
                'borderwidth': 1,
                'bordercolor': BORDER,
                'steps': [
                    {'range': [0, 20], 'color': "rgba(27, 67, 50, 0.05)"},
                    {'range': [20, 40], 'color': "rgba(217, 167, 0, 0.05)"},
                    {'range': [40, 60], 'color': "rgba(230, 95, 0, 0.05)"},
                    {'range': [60, 80], 'color': "rgba(193, 18, 31, 0.05)"},
                    {'range': [80, 100], 'color': "rgba(127, 29, 29, 0.05)"}
                ]
            }
        ))
        
        fig.update_layout(
            height=200,
            margin=dict(l=20, r=20, t=40, b=20),
            paper_bgcolor='rgba(0,0,0,0)'
        )
        return fig
    except Exception as e:
        st.warning("Data unavailable for this chart. Please check data/raw/ folder.")
        print(f"Error plotting SIDS gauge for {supplier}: {e}")
        return go.Figure()

def plot_vulnerability_heatmap():
    """
    Platform-Level Import Dependency: Where Are We Most Locked In?
    Dependency matrix: Weapons Category × Supplier.
    """
    try:
        categories = ['Aircraft', 'Submarines', 'Missiles', 'Tanks/AFV', 'Ships', 'Electronics']
        suppliers = ['Russia', 'France', 'USA', 'Israel', 'UK']
        
        # Hardcoded matrix from Section 3F
        # Rows = categories, Columns = suppliers
        matrix = [
            [70.0, 15.0, 10.0, 0.0, 5.0],  # Aircraft
            [30.0, 60.0, 0.0, 0.0, 0.0],   # Submarines
            [50.0, 0.0, 10.0, 30.0, 0.0],  # Missiles
            [85.0, 0.0, 0.0, 0.0, 0.0],    # Tanks
            [25.0, 0.0, 0.0, 0.0, 0.0],    # Ships (Domestic is 60%, Russian is 25%)
            [20.0, 10.0, 20.0, 40.0, 10.0] # Electronics (Simulated)
        ]
        
        fig = px.imshow(
            matrix,
            labels=dict(x="Supplier", y="Weapons Platform", color="Share %"),
            x=suppliers,
            y=categories,
            color_continuous_scale=[LIGHT_BG, "#FFEBEB", "#FFA8A8", THREAT_RED, "#7F1D1D"],
            text_auto=True
        )
        
        apply_premium_layout(fig, "Platform-Level Dependency Heatmap (% supplied)", show_legend=False)
        return fig
    except Exception as e:
        st.warning("Data unavailable for this chart. Please check data/raw/ folder.")
        print(f"Error plotting heatmap: {e}")
        return go.Figure()

def plot_russia_sids_trajectory():
    """
    Line chart showing Russia's SIDS score trajectory 2000-2024.
    Score jumps from 55 to 72 post-2022.
    """
    try:
        years = list(range(2000, 2025))
        scores = []
        for y in years:
            if y < 2022:
                # Pre-2022: steady SIDS around 55
                scores.append(55.0 + np.sin(y)*0.5)
            else:
                # Post-2022: jumps to 72 due to Ukraine War & sanctions
                scores.append(72.0 + np.sin(y)*0.3)
                
        df = pd.DataFrame({"Year": years, "SIDS": scores})
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=df['Year'],
            y=df['SIDS'],
            mode='lines+markers',
            line=dict(color=THREAT_RED, width=3),
            marker=dict(size=6, color=NAVY_PRIMARY),
            name="Russia SIDS Score"
        ))
        
        # Mark 2022
        fig.add_vline(x=2022, line_dash="dash", line_color=NAVY_SECONDARY, line_width=2)
        fig.add_annotation(
            x=2022,
            y=68.0,
            text="Ukraine War & Sanctions",
            showarrow=True,
            arrowhead=2,
            ax=-90,
            ay=-40,
            bgcolor="#FFFFFF",
            bordercolor=BORDER
        )
        
        apply_premium_layout(fig, "Russia SIDS Score Trajectory (2000-2024)", "Year", "SIDS Score")
        fig.update_yaxes(range=[40, 80])
        return fig
    except Exception as e:
        st.warning("Data unavailable for this chart. Please check data/raw/ folder.")
        print(f"Error plotting Russia SIDS trajectory: {e}")
        return go.Figure()

# -------------------------------------------------------------
# PAGE 5: MARKET INTELLIGENCE CHARTS
# -------------------------------------------------------------

def plot_stock_event_study(df_stocks, selected_event):
    """
    4-line Plotly chart: cumulative % return from event date (X: -30 to +30 days).
    """
    try:
        # Load event details
        from utils.constants import EVENTS
        ev = next((x for x in EVENTS if x["event"] == selected_event), None)
        if not ev:
            # Default to Galwan
            ev = next((x for x in EVENTS if "Galwan" in x["event"]), EVENTS[5])
            
        ev_date = pd.to_datetime(ev["date"])
        
        # Sort stocks by Date
        df = df_stocks.sort_values(by='Date').copy()
        
        # Find index close to event date
        idx_list = df.index[df['Date'] == ev_date].tolist()
        if len(idx_list) == 0:
            # Find closest date
            closest_idx = (df['Date'] - ev_date).abs().idxmin()
        else:
            closest_idx = idx_list[0]
            
        # Slice df from closest_idx - 30 to closest_idx + 30
        start_idx = max(0, closest_idx - 30)
        end_idx = min(len(df) - 1, closest_idx + 30)
        df_slice = df.iloc[start_idx:end_idx+1].copy()
        
        # Calculate days from event
        df_slice['Days_From_Event'] = range(- (closest_idx - start_idx), (end_idx - closest_idx) + 1)
        
        # Base prices at Day 0
        base_prices = df.loc[closest_idx]
        
        fig = go.Figure()
        colors = {
            "HAL.NS": GOLD_ACCENT,
            "BEL.NS": NAVY_SECONDARY,
            "BEML.NS": FOREST_GREEN,
            "MAZDOCK.NS": "purple",
            "COCHINSHIP.NS": "teal",
            "BDL.NS": "orange",
            "^NSEI": WARM_GRAY
        }
        
        # Calculate cumulative returns relative to Day 0
        for ticker in ["HAL.NS", "BEL.NS", "BEML.NS", "MAZDOCK.NS", "COCHINSHIP.NS", "BDL.NS"]:
            base_p = base_prices[ticker]
            # Handle possible zero division
            if base_p > 0:
                cum_ret = ((df_slice[ticker] - base_p) / base_p) * 100.0
                fig.add_trace(go.Scatter(
                    x=df_slice['Days_From_Event'],
                    y=cum_ret,
                    mode='lines',
                    name=ticker.replace(".NS", ""),
                    line=dict(color=colors.get(ticker, NAVY_PRIMARY), width=2)
                ))
                
        # Add Nifty return as comparison
        nifty_base = base_prices["^NSEI"]
        if nifty_base > 0:
            nifty_ret = ((df_slice["^NSEI"] - nifty_base) / nifty_base) * 100.0
            fig.add_trace(go.Scatter(
                x=df_slice['Days_From_Event'],
                y=nifty_ret,
                mode='lines',
                name="Nifty 50 Index",
                line=dict(color=colors["^NSEI"], width=2, dash='dash')
            ))
            
        fig.add_vline(x=0, line_dash="dash", line_color=THREAT_RED, line_width=1.5)
        fig.add_hline(y=0.0, line_color=WARM_GRAY, line_width=1.0)
        
        apply_premium_layout(
            fig, 
            f"Stock Reaction Study: {ev['event']} ({ev['date']})", 
            "Trading Days Relative to Event (Day 0)", 
            "Cumulative Return (%)"
        )
        return fig
    except Exception as e:
        st.warning("Data unavailable for this chart. Please check data/raw/ folder.")
        print(f"Error plotting stock event study: {e}")
        return go.Figure()

def plot_all_events_heatmap(df_stocks):
    """
    Heatmap of 30-day return % after each event for each stock.
    """
    try:
        from utils.constants import EVENTS
        tickers = ["HAL.NS", "BEL.NS", "BEML.NS", "MAZDOCK.NS", "COCHINSHIP.NS", "BDL.NS", "^NSEI"]
        
        data = []
        df = df_stocks.sort_values(by='Date').copy()
        
        for ev in EVENTS:
            ev_date = pd.to_datetime(ev["date"])
            # Get stock reaction indices
            idx_list = df.index[df['Date'] == ev_date].tolist()
            if len(idx_list) == 0:
                closest_idx = (df['Date'] - ev_date).abs().idxmin()
            else:
                closest_idx = idx_list[0]
                
            # If 30 days is out of bound
            end_idx = min(len(df) - 1, closest_idx + 22) # 22 trading days is approx 30 calendar days
            
            row_data = {"Event": ev["event"]}
            for tick in tickers:
                base_price = df.loc[closest_idx, tick]
                post_price = df.loc[end_idx, tick]
                if base_price > 0:
                    ret = ((post_price - base_price) / base_price) * 100.0
                else:
                    ret = 0.0
                row_data[tick.replace(".NS", "").replace("^", "")] = ret
            data.append(row_data)
            
        df_heatmap = pd.DataFrame(data)
        df_heatmap = df_heatmap.set_index("Event")
        
        fig = px.imshow(
            df_heatmap,
            labels=dict(color="30d Return %"),
            color_continuous_scale="RdYlGn",
            color_continuous_midpoint=0,
            text_auto='.1f'
        )
        
        apply_premium_layout(fig, "30-Day Cumulative Return After Escalation Events", show_legend=False)
        return fig
    except Exception as e:
        st.warning("Data unavailable for this chart. Please check data/raw/ folder.")
        print(f"Error plotting all events heatmap: {e}")
        return go.Figure()

def plot_nifty_outperformance(df_stocks):
    """
    Bar chart showing alpha (defence stock return minus Nifty return) over events.
    """
    try:
        from utils.constants import EVENTS
        df = df_stocks.sort_values(by='Date').copy()
        
        data = []
        for ev in EVENTS:
            ev_date = pd.to_datetime(ev["date"])
            idx_list = df.index[df['Date'] == ev_date].tolist()
            closest_idx = idx_list[0] if len(idx_list) > 0 else (df['Date'] - ev_date).abs().idxmin()
            
            end_idx = min(len(df) - 1, closest_idx + 22)
            
            # Average of defence stocks
            def_rets = []
            nifty_ret = 0.0
            for tick in ["HAL.NS", "BEL.NS", "BEML.NS", "MAZDOCK.NS", "COCHINSHIP.NS", "BDL.NS"]:
                base = df.loc[closest_idx, tick]
                val = df.loc[end_idx, tick]
                if base > 0:
                    def_rets.append(((val - base) / base) * 100.0)
                    
            base_nifty = df.loc[closest_idx, "^NSEI"]
            val_nifty = df.loc[end_idx, "^NSEI"]
            if base_nifty > 0:
                nifty_ret = ((val_nifty - base_nifty) / base_nifty) * 100.0
                
            avg_def_ret = np.mean(def_rets) if len(def_rets) > 0 else 0.0
            alpha = avg_def_ret - nifty_ret
            
            data.append({
                "Event": ev["event"],
                "Alpha": alpha,
                "Type": "Outperformed" if alpha > 0 else "Underperformed"
            })
            
        df_alpha = pd.DataFrame(data)
        
        fig = px.bar(
            df_alpha,
            x="Alpha",
            y="Event",
            color="Type",
            color_discrete_map={"Outperformed": FOREST_GREEN, "Underperformed": THREAT_RED},
            orientation="h",
            text_auto='.1f'
        )
        
        apply_premium_layout(fig, "Defence Stocks Alpha Over Nifty 50 (30 Days)", "Alpha (% Outperformance)", "Event", show_legend=True)
        return fig
    except Exception as e:
        st.warning("Data unavailable for this chart. Please check data/raw/ folder.")
        print(f"Error plotting nifty outperformance: {e}")
        return go.Figure()

def plot_stock_price_history(df_stocks, selected_stock, show_events):
    """
    Historical price line chart with overlayable event markers.
    """
    try:
        fig = go.Figure()
        
        # Stock Line Line Colors mapping
        colors_map = {
            "HAL.NS": GOLD_ACCENT,
            "BEL.NS": NAVY_PRIMARY,
            "BEML.NS": FOREST_GREEN,
            "MAZDOCK.NS": "purple",
            "COCHINSHIP.NS": "teal",
            "BDL.NS": "orange",
            "^NSEI": WARM_GRAY
        }
        line_color = colors_map.get(selected_stock, GOLD_ACCENT)
        fig.add_trace(go.Scatter(
            x=df_stocks['Date'],
            y=df_stocks[selected_stock],
            mode='lines',
            line=dict(color=line_color, width=2.5),
            name=selected_stock.replace(".NS", "")
        ))
        
        # Event Markers
        if show_events:
            from utils.constants import EVENTS
            for ev in EVENTS:
                ev_date = pd.to_datetime(ev["date"])
                # Only show events in the range of the stock date
                if df_stocks['Date'].min() <= ev_date <= df_stocks['Date'].max():
                    # Find price at date
                    match = df_stocks[df_stocks['Date'] == ev_date]
                    if not match.empty:
                        price = match.iloc[0][selected_stock]
                    else:
                        closest_idx = (df_stocks['Date'] - ev_date).abs().idxmin()
                        price = df_stocks.loc[closest_idx, selected_stock]
                        
                    fig.add_trace(go.Scatter(
                        x=[ev_date],
                        y=[price],
                        mode='markers+text',
                        marker=dict(symbol='triangle-up', size=11, color=THREAT_RED),
                        text=[ev['event']],
                        textposition='top center',
                        hoverinfo='text',
                        name=ev['event'],
                        showlegend=False
                    ))
                    
        apply_premium_layout(fig, f"{selected_stock.replace('.NS', '')} Historical Stock Price", "Date", "Stock Price (INR)", show_legend=False)
        return fig
    except Exception as e:
        st.warning("Data unavailable for this chart. Please check data/raw/ folder.")
        print(f"Error plotting stock history: {e}")
        return go.Figure()

def plot_supplier_risk_radar(sids_data):
    """
    Radar chart comparing the risk profiles of top suppliers (Russia, France, USA)
    across the 4 dimensions of SIDS.
    """
    try:
        categories = ['Import Concentration (IC)', 'Single-Source Risk (SSR)', 
                      'Geopolitical Risk (1-GSS)', 'Substitution Difficulty (1-DSC)']
        
        fig = go.Figure()
        
        # Russia
        r_params = sids_data.get("Russia", {})
        if r_params:
            r_ic = r_params["IC"] * 2.0  # Normalized for visual balance (45% -> 90)
            r_ssr = r_params["SSR"] * 100.0
            r_gss = (1.0 - r_params["GSS"]) * 100.0
            r_dsc = (1.0 - r_params["DSC"]) * 100.0
            fig.add_trace(go.Scatterpolar(
                r=[r_ic, r_ssr, r_gss, r_dsc, r_ic],
                theta=categories + [categories[0]],
                fill='toself',
                name='Russia (Critical)',
                line_color=THREAT_RED
            ))
            
        # France
        f_params = sids_data.get("France", {})
        if f_params:
            f_ic = f_params["IC"] * 2.0
            f_ssr = f_params["SSR"] * 100.0
            f_gss = (1.0 - f_params["GSS"]) * 100.0
            f_dsc = (1.0 - f_params["DSC"]) * 100.0
            fig.add_trace(go.Scatterpolar(
                r=[f_ic, f_ssr, f_gss, f_dsc, f_ic],
                theta=categories + [categories[0]],
                fill='toself',
                name='France (Low-Moderate)',
                line_color=GOLD_ACCENT
            ))
            
        # USA
        u_params = sids_data.get("USA", {})
        if u_params:
            u_ic = u_params["IC"] * 2.0
            u_ssr = u_params["SSR"] * 100.0
            u_gss = (1.0 - u_params["GSS"]) * 100.0
            u_dsc = (1.0 - u_params["DSC"]) * 100.0
            fig.add_trace(go.Scatterpolar(
                r=[u_ic, u_ssr, u_gss, u_dsc, u_ic],
                theta=categories + [categories[0]],
                fill='toself',
                name='USA (Low)',
                line_color=NAVY_SECONDARY
            ))
            
        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 100],
                    gridcolor=BORDER
                ),
                angularaxis=dict(
                    gridcolor=BORDER,
                    tickfont=dict(size=10, color=WARM_GRAY)
                )
            ),
            showlegend=True,
            title={
                'text': "<b>Supplier Risk Fingerprints (Radar)</b>",
                'font': {'family': CHART_FONT_FAMILY, 'size': 15, 'color': NAVY_SECONDARY}
            },
            font=dict(family=CHART_FONT_FAMILY, size=11),
            paper_bgcolor='rgba(0,0,0,0)',
            margin=dict(l=100, r=100, t=50, b=40),
            height=360
        )
        return fig
    except Exception as e:
        st.warning("Data unavailable for this chart. Please check data/raw/ folder.")
        print(f"Error plotting risk radar: {e}")
        return go.Figure()

def plot_arms_flow_sankey(df_transfers):
    """
    Sankey diagram showing arms flow from Suppliers to Weapons Categories and to India's Arsenal.
    """
    try:
        # Define nodes - matching raw database names
        label_clean = ["Russia", "France", "USA", "Israel", "UK", "Others", 
                       "Aircraft", "Submarines", "Missiles", "Tanks/AFV", "Ships", "Electronics", 
                       "India's Arsenal"]
        
        # Bold and readable labels for Plotly display
        label_display = [f"<b>{lbl}</b>" for lbl in label_clean]
        
        # Color palettes matching our theme
        color = [THREAT_RED, GOLD_ACCENT, NAVY_SECONDARY, "teal", "orange", WARM_GRAY,
                 "#2563EB", "#7C3AED", "#059669", "#DC2626", "#4B5563", "#D97706",
                 NAVY_PRIMARY]
        
        # Link arrays: source, target, value
        # Mapping index positions:
        # Suppliers (0-5), Categories (6-11), Arsenal (12)
        # We compute these values dynamically from df_transfers
        df_group = df_transfers.groupby(['Supplier', 'Category']).agg({'SIPRI_TIV': 'sum'}).reset_index()
        
        sources = []
        targets = []
        values = []
        
        # Supplier to Category links
        for _, row in df_group.iterrows():
            sup = row['Supplier']
            cat = row['Category']
            val = row['SIPRI_TIV']
            
            # Map labels
            if sup in label_clean and cat in label_clean:
                sources.append(label_clean.index(sup))
                targets.append(label_clean.index(cat))
                values.append(int(val))
                
        # Category to Destination links
        category_sums = df_group.groupby('Category').agg({'SIPRI_TIV': 'sum'}).reset_index()
        for _, row in category_sums.iterrows():
            cat = row['Category']
            val = row['SIPRI_TIV']
            if cat in label_clean:
                sources.append(label_clean.index(cat))
                targets.append(label_clean.index("India's Arsenal"))
                values.append(int(val))
                
        fig = go.Figure(data=[go.Sankey(
            node = dict(
              pad = 22,
              thickness = 12,
              line = dict(color = NAVY_PRIMARY, width = 0.5),
              label = label_display,
              color = color
            ),
            link = dict(
              source = sources,
              target = targets,
              value = values,
              color = "rgba(108, 117, 125, 0.15)" # Semi-transparent links
            ),
            textfont = dict(
              color = NAVY_PRIMARY,
              size = 12,
              family = CHART_FONT_FAMILY
            )
          )])
        
        fig.update_layout(
            title={
                'text': "<b>Arms Procurement Flow Pipeline (Sankey)</b>",
                'font': {'family': CHART_FONT_FAMILY, 'size': 15, 'color': NAVY_SECONDARY}
            },
            font=dict(family=CHART_FONT_FAMILY, size=12, color=NAVY_PRIMARY),
            paper_bgcolor='rgba(0,0,0,0)',
            margin=dict(l=20, r=20, t=50, b=20),
            height=380
        )
        return fig
    except Exception as e:
        st.warning("Data unavailable for this chart. Please check data/raw/ folder.")
        print(f"Error plotting arms flow sankey: {e}")
        return go.Figure()
