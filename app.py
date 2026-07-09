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
st.title("🏛️ VTVA Event Financial Summary")
st.info("This dashboard provides a transparent view of the recent community event's financial performance.")

# --- DATA PREPARATION ---
# Edit these numbers whenever you need to update the site
total_exp = 4614.31
donations = 2001.00
net_funding = total_exp - donations

# --- 3. KEY METRICS ---
c1, c2, c3 = st.columns(3)
c1.metric("Total Expenses", f"${total_exp:,.2f}")
c2.metric("Total Donations", f"${donations:,.2f}")
c3.metric("Net Funding Required", f"${net_funding:,.2f}", delta_color="inverse")

st.divider()

# --- 4. EXPENSE CHART ---
st.subheader("📊 Expense Distribution")

chart_data = {
    "Category": [
        "Supplies & Grocery", 
        "Catering Setup", 
        "Operations (Priests/Security)", 
        "Sweets (Laddus)", 
        "A/V & Admin"
    ],
    "Amount": [1820.60, 1160.58, 1160.00, 275.26, 197.87]
}
df = pd.DataFrame(chart_data)

# Create Chart with Premium Colors (Golden/Navy palette)
fig = px.bar(
    df, 
    x="Amount", 
    y="Category", 
    orientation='h',
    text="Amount",
    color_discrete_sequence=['#D4AF37'] # Professional Gold color
)

# Proper Amount Formatting on the chart
fig.update_traces(
    texttemplate='$%{text:,.2f}', 
    textposition='outside',
    marker_line_color='#1f3b4d',
    marker_line_width=1.5,
    opacity=0.8
)

fig.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    xaxis_title="Amount in USD ($)",
    yaxis_title="",
    xaxis_showgrid=True,
    gridcolor='#e1e1e1',
    font=dict(size=14),
    margin=dict(l=20, r=100, t=20, b=20), # Extra space for labels on mobile
    height=400
)

st.plotly_chart(fig, use_container_width=True)

# --- 5. FOOTER ---
st.divider()
st.caption("✅ Financial data verified by VTVA Treasury. For internal community review only.")
