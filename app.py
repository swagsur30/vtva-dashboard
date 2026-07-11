import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Page Config
st.set_page_config(page_title="VTVA Financials", layout="centered", page_icon="💰")

# Custom CSS optimized for BOTH Light and Dark Mobile themes
st.markdown("""
    <style>
    /* Metric label & value adaptation */
    div[data-testid="stMetricValue"] { 
        font-size: 26px !important; 
    }
    /* Devotional box that respects light/dark background contrast safely */
    .vasavi-box {
        text-align: center;
        background-color: rgba(255, 249, 230, 0.15);
        border: 2px solid #ffcc80;
        padding: 10px;
        border-radius: 8px;
        margin-bottom: 15px;
    }
    .vasavi-title {
        font-size: 18px; 
        font-weight: bold; 
        color: #b37400; 
        letter-spacing: 0.5px;
    }
    /* Subtitle styling that works on dark and light phone screens */
    .mobile-subtitle {
        font-size: 16px;
        font-weight: 500;
        margin-top: -15px;
        margin-bottom: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- GLOBAL RUNTIME HIT COUNTER (PERSISTENT ACROSS SESSIONS) ---
@st.cache_resource
def get_global_counter():
    # Shared across all user sessions in server memory
    return {"views": 45}

global_counter = get_global_counter()

# Increment only once when a user initializes their tab session
if 'counted_this_session' not in st.session_state:
    global_counter["views"] += 1
    st.session_state['counted_this_session'] = True

live_views = global_counter["views"]

# 2. Header Section
st.title("🏛️ VTVA Kalyanam Event Financial Summary")
st.markdown('<p class="mobile-subtitle">📅 Event Date: June 7, 2026</p>', unsafe_allow_html=True)

# --- CONDENSED COMMUNITY DEDICATION SECTION ---
st.divider()
col1, col2, col3 = st.columns([0.5, 5, 0.5])
with col2:
    st.markdown(
        """
        <div class="vasavi-box">
            <span class="vasavi-title">🙏 Jai Vasavi Matha 🙏</span>
            <div style="font-size: 13px; font-style: italic; margin-top: 4px;">
                Seeking the divine blessings of Sri Vasavi Matha
            </div>
        </div>
        """, 
        unsafe_allow_html=True
    )

st.info("This dashboard provides a transparent view of the recent community event's financial performance.")

# --- UPDATED DATA PREPARATION ---
total_exp = 4692.16
donations = 2001.00
net_funding = total_exp - donations

# --- 3. KEY METRICS ---
c1, c2, c3 = st.columns(3)
c1.metric("Total Expenses", f"${total_exp:,.2f}")
c2.metric("Total Donations", f"${donations:,.2f}")
c3.metric("VTVA Funds Used", f"${net_funding:,.2f}")

st.divider()

# --- 4. EXPENSE CHART & DATA ---
st.subheader("📊 Detailed Expense Distribution")

chart_data = {
    "Category": [
        "Food Procurement & Supplies",
        "Venue Operations & Cleaning",
        "Pooja Supplies & Flowers",
        "Priest Dakshina",
        "Audio/Visual & Vastram",
        "Venue Cooking Helpers",
        "Miscellaneous (Dollar Store, Walmart, Home Depot)"
    ],
    "Amount": [1885.87, 860.00, 630.52, 300.00, 197.87, 150.00, 77.85]
}
df_exp = pd.DataFrame(chart_data)
df_exp_sorted = df_exp.sort_values(by="Amount", ascending=True)

# Plotly Horizontal Bar Chart
fig = px.bar(
    df_exp_sorted, 
    x="Amount", 
    y="Category", 
    orientation='h',
    text="Amount",
    color_discrete_sequence=['#D4AF37']
)

fig.update_traces(
    texttemplate='$%{text:,.2f}', 
    textposition='inside', # High-contrast text position inside the bars for small mobile screens
    textfont=dict(size=12), 
    marker_line_color='#1f3b4d',
    marker_line_width=1,
    opacity=0.9
)

fig.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    xaxis=dict(
        title="Amount in USD ($)",
        showgrid=True,
        gridcolor='rgba(128, 128, 128, 0.2)' # Adaptive soft grid lines
    ),
    yaxis=dict(title=""),
    font=dict(size=12), 
    margin=dict(l=10, r=10, t=15, b=15), 
    height=450 
)

st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})

# --- EXPANDABLE DATA BREAKDOWN ---
with st.expander("🔍 View Raw Breakdown & Export Data"):
    df_display = df_exp.sort_values(by="Amount", ascending=False).copy()
    df_display["Amount"] = df_display["Amount"].map("${:,.2f}".format)
    
    st.dataframe(df_display, use_container_width=True, hide_index=True)
    
    csv = df_exp.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download Expense Report (CSV)",
        data=csv,
        file_name="VTVA_Kalyanam_Expenses.csv",
        mime="text/csv"
    )

# --- 5. FOOTER ---
st.divider()

foot_c1, foot_c2 = st.columns([2, 1])
with foot_c1:
    st.caption("✅ Financial data verified by VTVA Treasury. Internal review only.")

with foot_c2:
    st.markdown(
        f'<div style="text-align: right; font-size: 12px; color: #2e7d32; font-weight: bold;">'
        f'📈 Hits: {live_views}'
        f'</div>', 
        unsafe_allow_html=True
    )
