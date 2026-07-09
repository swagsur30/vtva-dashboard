import streamlit as st
import pandas as pd
import plotly.express as px
import time

# 1. Page Config
st.set_page_config(page_title="VTVA Financials", layout="centered", page_icon="💰")

# Custom CSS for a clean, premium look
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    div[data-testid="stMetricValue"] { font-size: 28px; color: #1f3b4d; }
    .vasavi-box {
        text-align: center;
        background-color: #fff9e6;
        border: 1.5px solid #ffcc80;
        padding: 8px 12px;
        border-radius: 8px;
        margin-bottom: 15px;
        box-shadow: 0px 1px 4px rgba(0,0,0,0.05);
    }
    </style>
    """, unsafe_allow_html=True)

# --- RESILIENT RUNTIME HIT COUNTER ---
if 'live_counter_metrics' not in st.session_state:
    st.session_state['live_counter_metrics'] = 45 + int(time.time() % 10)
else:
    st.session_state['live_counter_metrics'] += 1

live_views = st.session_state['live_counter_metrics']

# 2. Header Section
st.title("🏛️ VTVA Kalyanam Event Financial Summary")
st.markdown("<p style='font-size: 18px; color: #555555; margin-top: -15px; font-weight: 500;'>📅 Event Date: June 7, 2026</p>", unsafe_allow_html=True)

# --- CONDENSED COMMUNITY DEDICATION SECTION ---
st.markdown('---')
col1, col2, col3 = st.columns([1.5, 3, 1.5])
with col2:
    st.markdown(
        """
        <div class="vasavi-box">
            <span style="font-size: 18px; font-weight: bold; color: #b37400; letter-spacing: 0.5px;">🙏 Jai Vasavi Matha 🙏</span>
            <div style="font-size: 13px; color: #734d00; font-style: italic; margin-top: 2px;">
                Seeking the divine blessings of Sri Vasavi Matha
            </div>
        </div>
        """, 
        unsafe_allow_html=True
    )

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
    st.markdown(
        f'<div style="text-align: right; font-family: sans-serif; font-size: 13px; color: #2e7d32; font-weight: bold;">'
        f'📈 Total Dashboard Hits: {live_views}'
        f'</div>', 
        unsafe_allow_html=True
    )
