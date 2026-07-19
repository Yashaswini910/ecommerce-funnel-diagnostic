
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="E-Commerce Funnel Diagnostic", layout="wide")

st.title("🛒 E-Commerce Cart Abandonment Funnel Diagnostic")
st.markdown("### *Enterprise-Grade Pipeline Operations & Leakage Diagnostics*")
st.write("---")

# 1. SIDEBAR SIMULATION PARAMETERS
st.sidebar.header("🎯 Optimization Simulation Parameters")
recovery_rate = st.sidebar.slider(
    "Target Recovery Volume (%)", 
    min_value=5, max_value=100, value=25, step=5
) / 100.0

st.sidebar.markdown("""
**Diagnostic Context:**
* **Technical Patch:** Restores Mobile Safari iOS form focus handling.
* **Marketing Patch:** Aligns dynamic checkout pricing with programmatic ad content.
""")

# 2. GENERATE WORKING KPI METRICS (Mocking the Live Cloud Aggregates)
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Global Baseline AOV", value="$84.72", delta="+2.4% vs Last Month")
with col2:
    st.metric(label="Identified UI Drop-Offs (US-West)", value="684 Sessions", delta="-14.2% Attrition", delta_color="inverse")
with col3:
    # Programmatic impact based on dynamic user input
    simulated_recovery = int(684 * recovery_rate)
    recovered_rev = simulated_recovery * 84.72
    st.metric(label="Recoverable Revenue Potential", value=f"${recovered_rev:,.2f}", delta=f"+{simulated_recovery} Converted Orders")

st.write("---")

# 3. INTERACTIVE VISUAL ZONE
st.subheader("📊 Funnel Retention Analysis: Baseline vs Anomaly Cohorts")

# Generate standard data arrays for visualization
steps = ['1. View Item', '2. Add to Cart', '3. Enter Shipping', '4. Enter Payment', '5. Purchase Complete']
baseline_retention = [100.0, 48.2, 36.1, 28.4, 4.1]
safari_retention = [100.0, 49.0, 12.2, 8.5, 1.2]

fig, ax = plt.subplots(figsize=(10, 4.5))
x = np.arange(len(steps))
width = 0.35

ax.bar(x - width/2, baseline_retention, width, label='Baseline Traffic Profile', color='#2b5c8f', alpha=0.85)
ax.bar(x + width/2, safari_retention, width, label='US-West Mobile Safari Cohort', color='#d9534f', alpha=0.85)

ax.set_ylabel('Funnel Retention (%)', fontsize=10, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(steps, fontsize=9)
ax.legend(frameon=True, facecolor='white')
ax.set_ylim(0, 110)

# Annotation for specific UI rendering issue
ax.annotate('75% Systemic Breakpoint', 
            xy=(2.15, 12.2), 
            xytext=(2.6, 40),
            arrowprops=dict(facecolor='#d9534f', shrink=0.05, width=1.5, headwidth=6))

st.pyplot(fig)

st.write("---")

# 4. DATA TABLE DRILLDOWN
st.subheader("🔍 Dimensional Performance Ledger")
data_ledger = {
    "Dimension": ["Device Type", "Device Type", "Browser", "Browser", "Traffic Source"],
    "Segment Value": ["Desktop", "Mobile", "Chrome", "Safari", "Facebook-Ads"],
    "S1 to S2 (Cart %)_": ["47.8%", "49.2%", "48.1%", "48.5%", "88.4%"],
    "S2 to S3 (Shipping %)_": ["72.1%", "41.3%", "70.4%", "34.1%", "71.2%"],
    "S3 to S4 (Payment %)_": ["81.4%", "78.2%", "82.0%", "52.3%", "9.1%"],
    "Overall Conversion": ["4.3%", "1.6%", "4.4%", "1.1%", "0.8%"]
}
df_ledger = pd.DataFrame(data_ledger)
st.dataframe(df_ledger, use_container_width=True)
