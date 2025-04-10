import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="NUCLIREGEN-P | Global & Economic Impact", layout="wide", page_icon="🌍")

# Modo oscuro total
st.markdown("""
    <style>
        body, .stApp {
            background-color: #0d1117;
            color: #ffffff;
        }
        .block-container { padding: 2rem; }
        h1, h2, h3, h4, h5 {
            color: #00ffff;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🌍 NUCLIREGEN-P: Global Prevalence, Cost & Access Dashboard")

# ---------- Mapa Interactivo Mundial ----------
st.subheader("🗺️ Global Prevalence & Therapy Access")
global_data = pd.DataFrame({
    "Country": ["Ecuador", "USA", "India", "Nigeria", "Peru", "South Africa", "Germany"],
    "Code": ["ECU", "USA", "IND", "NGA", "PER", "ZAF", "DEU"],
    "Estimated Prevalence": [32, 75, 150, 110, 40, 52, 28],
    "Access to Therapy (%)": [25, 90, 30, 20, 40, 35, 80],
    "Priority Level": ["High", "Low", "High", "High", "Medium", "Medium", "Low"]
})

fig_map = px.choropleth(
    global_data,
    locations="Code",
    color="Estimated Prevalence",
    hover_name="Country",
    color_continuous_scale="plasma",
    title="Estimated Prevalence of Progeria and Therapy Access",
    labels={'Estimated Prevalence': 'Cases'},
    template="plotly_dark"
)
fig_map.update_geos(showframe=False, showcoastlines=False)
fig_map.update_layout(height=600, margin=dict(l=0, r=0, t=50, b=0))

st.plotly_chart(fig_map, use_container_width=True)

# ---------- Gráfico de barras: Costo por paciente ----------
st.subheader("💰 Cost per Patient Comparison")
cost_df = pd.DataFrame({
    "Therapy": ["NUCLIREGEN-P", "Lonafarnib", "CRISPR"],
    "Cost (USD)": [8000, 100000, 500000]
})

bar_fig = px.bar(
    cost_df,
    x="Therapy",
    y="Cost (USD)",
    color="Therapy",
    text="Cost (USD)",
    color_discrete_sequence=["#00ffff", "#ffaa00", "#ff004c"],
    template="plotly_dark"
)
bar_fig.update_layout(height=500, xaxis_title="Therapy Type", yaxis_title="USD per Treatment")
bar_fig.update_traces(texttemplate='$%{y:,.0f}', textposition='outside')

st.plotly_chart(bar_fig, use_container_width=True)

# ---------- Esquema de distribución solidaria ----------
st.subheader("🔄 One-for-One Solidarity Distribution Flow")
flow_fig = go.Figure()
flow_fig.add_trace(go.Sankey(
    node=dict(
        pad=15,
        thickness=20,
        line=dict(color="black", width=0.5),
        label=["High-Income Countries", "Low-Income Recipients", "NUCLIREGEN Treatments", "Donation System"],
        color=["#00ffff", "#ffaa00", "#04d9ff", "#ff69b4"]
    ),
    link=dict(
        source=[0, 0, 3],  # From nodes
        target=[2, 3, 1],  # To nodes
        value=[100, 100, 100],
        color=["#00ffff", "#ff69b4", "#ffaa00"]
    )
))
flow_fig.update_layout(title_text="Solidarity Flow: One-for-One NUCLIREGEN-P Distribution", font_size=14, height=500, template="plotly_dark")
st.plotly_chart(flow_fig, use_container_width=True)

# Footer
st.markdown("""
    <hr style='border: 1px solid #00ffff;'>
    <p style='text-align: center; color: #aaa;'>Part of NUCLIREGEN-P | Global Health Equity & Precision Medicine Initiative</p>
""", unsafe_allow_html=True)
