import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Page Configuration (Sets title and wide layout)
st.set_page_config(page_title="VTVA Event Dashboard", layout="centered", page_icon="📊")

# 2. Main Title
st.title("📊 VTVA Event Financial Dashboard")
st.markdown("A high-level summary of expenses and donations for the recent community event.")
st.markdown("---")

# 3. Quick Summary Cards (Key Metrics)
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Total Expenses", value="$4,614.31")
with col2:
    st.metric(label="Total Donations", value="$2,001.00")
with col3:
    st.metric(label="Net Funding Required", value="$2,613.31")

st.markdown("---")
st.markdown("### 📈 Expense Breakdown by Category")

# 4. Preparing the Data for Charting
data = {
    "Category": [
        "Supplies, Flowers & Grocery", 
        "Food & Catering Setup", 
        "Event Operations (Priests, Security, Cleaners)", 
        "Sweets Prep (Laddus)", 
        "A/V & Admin (DJ, etc.)"
    ],
    "Amount": [1820.60, 1160.58, 1160.00, 275.26, 197.87]
}
df = pd.DataFrame(data)

# 5. Creating an Interactive Horizontal Bar Chart
fig = px.bar(
    df, 
    x="Amount", 
    y="Category", 
    orientation='h', 
    text="Amount",
    color="Amount", 
    color_continuous_scale="Blues",
    labels={"Amount": "Amount ($)"}
)

# Customizing chart appearance
fig.update_traces(texttemplate='$%{text:,.2f}', textposition='outside')
fig.update_layout(
    yaxis={'categoryorder':'total ascending'}, 
    showlegend=False,
    margin=dict(l=20, r=50, t=20, b=20)
)

# Display chart in Streamlit app (Typo fixed here!)
st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
st.caption("📑 Data verified against the master spreadsheet 'Summary' tab.")