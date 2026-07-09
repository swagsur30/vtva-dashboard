import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Page Config
st.set_page_config(page_title="VTVA Financials", layout="centered", page_icon="💰")

# Custom CSS for a clean look
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    div[data-testid="stMetricValue"] { font-size: 28px; color: #1f3b4d; }
    </style>
    """, unsafe_allow_html=True)

# --- NATIVE VIEW COUNTER TRACKING ---
# Bypasses external image blockers by tracking session hits directly in Python memory
if 'view_count' not in st.session_state:
    st.session_state['view_count'] = 1
else:
    st.session_state['view_count'] += 1

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
df_exp = pd.DataFrame(chart_data)
df_exp = df_exp.sort_values(by="Amount", ascending=True)

fig = px.bar(
    df_exp, 
    x="Amount", 
    y="Category", 
    orientation='h',
    text="Amount",
    color_discrete_sequence=['#D4AF37']
)

# Text positions to 'auto' to ensure text slides cleanly outside the bars
fig.update_traces(
    texttemplate='$%{text:,.2f}', 
    textposition='auto',
    textfont=dict(color='black', size=13),
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
    yaxis=dict(title=""),
    font=dict(size=14),
    margin=dict(l=20, r=60, t=20, b=20), 
    height=450 
)

st.plotly_chart(fig, use_container_width=True)

# --- 5. FOOTER ---
st.divider()

foot_c1, foot_c2 = st.columns([3, 1])
with foot_c1:
    st.caption("✅ Financial data verified by VTVA Treasury. For internal community review only.")

with foot_c2:
    # Renders a clean, native text badge displaying the view metrics flawlessly on all phones
    st.markdown(
        f'<div style="text-align: right; font-family: monospace; font-size: 12px; color: #6c757d;">'
        f'📊 Page Views: <b>{st.session_state["view_count"]}</b>'
        f'</div>', 
        unsafe_allow_html=True
    )
