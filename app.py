import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Page Config
st.set_page_config(page_title="VTVA Financials", layout="centered", page_icon="💰")

# Custom CSS to make it look "Premium"
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    div[data-testid="stMetricValue"] { font-size: 28px; color: #1f3b4d; }
    </style>
    """, unsafe_allow_html=True)

# 2. Header Section
st.title("🏛️ VTVA Kalyanam Event Financial Summary")
st.info("This dashboard provides a transparent view of the recent community event's financial performance.")

# --- DATA PREPARATION ---
total_exp = 4614.31
donations = 2001.00
net_funding = total_exp - donations

# --- 3. KEY METRICS ---
c1, c2, c3 = st.columns(3)
c1.metric("Total Expenses", f"${total_exp:,.2f}")
c2.metric("Total Donations", f"${donations:,.2f}")
c3.metric("VTVA Funds Used", f"${net_funding:,.2f}", delta_color="inverse")

st.divider()

# --- 4. EXPENSE CHART ---
st.subheader("📊 Detailed Expense Distribution")

# Finalized category mapping incorporating laddus and kitchen/food handling supplies
chart_data = {
    "Category": [
        "Food Procurement, Ingredients, Laddus & Supplies",
        "Venue Operations & Cleaning",
        "Pooja Supplies & Flowers",
        "Priest Dakshina",
        "Audio/Visual & Vastram",
        "Venue Cooking Helpers"
    ],
    "Amount": [1885.87, 860.00, 630.52, 300.00, 197.87, 150.00]
}
df = pd.DataFrame(chart_data)

# Sort from largest to smallest for a polished display hierarchy
df = df.sort_values(by="Amount", ascending=True)

# Create Chart with Premium Colors (Golden/Navy palette)
fig = px.bar(
    df, 
    x="Amount", 
    y="Category", 
    orientation='h',
    text="Amount",
    color_discrete_sequence=['#D4AF37'] # Professional Gold color
)

# Proper Amount Formatting inside the bars for flawless mobile viewing
fig.update_traces(
    texttemplate='$%{text:,.2f}', 
    textposition='inside',
    textfont=dict(color='black', size=13),
    insidetextanchor='end', 
    marker_line_color='#1f3b4d',
    marker_line_width=1.5,
    opacity=0.8
)

fig.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    xaxis=dict(
        title="Amount in USD ($)",
        showgrid=True,
        gridcolor='#e1e1e1'
    ),
    yaxis=dict(
        title=""
    ),
    font=dict(size=14),
    margin=dict(l=20, r=20, t=20, b=20), 
    height=450 
)

st.plotly_chart(fig, use_container_width=True)

# --- 5. FOOTER ---
st.divider()

# Left column for verification note, right column for the live view counter badge
foot_c1, foot_c2 = st.columns([3, 1])
with foot_c1:
    st.caption("✅ Financial data verified by VTVA Treasury. For internal community review only.")

with foot_c2:
    st.markdown(
        '<div style="text-align: right;"><img src="https://counter.hits.io/vtva-dashboard.svg" alt="Hits"></div>', 
        unsafe_allow_html=True
    )
