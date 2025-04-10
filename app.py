import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="NUCLIREGEN-P | Global & Economic Impact", layout="wide", page_icon="🌍")

# Estilo Modo Oscuro Total
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
        .css-1aumxhk, .css-ffhzg2 {
            background-color: transparent !important;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🌍 NUCLIREGEN-P: Global 3D Impact Dashboard")

# ---------- Mapa Interactivo Mundial 3D ----------
st.subheader("🌐 3D Realistic Choropleth Map: Progeria Prevalence & Access")
global_data = pd.DataFrame({
    "Country": ["Ecuador", "USA", "India", "Nigeria", "Peru", "South Africa", "Germany"],
    "Code": ["ECU", "USA", "IND", "NGA", "PER", "ZAF", "DEU"],
    "Estimated Prevalence": [32, 75, 150, 110, 40, 52, 28],
    "Access to Therapy (%)": [25, 90, 30, 20, 40, 35, 80]
})

fig_map = px.choropleth(global_data,
    locations="Code",
    color="Estimated Prevalence",
    hover_name="Country",
    color_continuous_scale=px.colors.sequential.Plasma_r,
    projection="orthographic",
    template="plotly_dark",
    title="🌐 Estimated Prevalence of Progeria & Therapy Access")
fig_map.update_geos(showframe=True, showcoastlines=True, projection_type='orthographic')
fig_map.update_layout(height=650, margin=dict(l=0, r=0, t=50, b=0))

st.plotly_chart(fig_map, use_container_width=True)

# ---------- Gráfico de barras: Costo por paciente ----------
st.subheader("💰 Dynamic Cost Comparison per Patient")
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
    template="plotly_dark",
    title="💰 Cost per Patient: NUCLIREGEN vs. Others"
)
bar_fig.update_layout(
    height=500,
    xaxis_title="Therapy Type",
    yaxis_title="USD per Treatment",
    font=dict(color="white")
)
bar_fig.update_traces(texttemplate='$%{y:,.0f}', textposition='outside')

st.plotly_chart(bar_fig, use_container_width=True)

# ---------- Esquema de distribución solidaria avanzado ----------
st.subheader("🔄 High-Impact One-for-One Solidarity Flow")
flow_fig = go.Figure(go.Sankey(
    node=dict(
        pad=20,
        thickness=30,
        line=dict(color="black", width=0.5),
        label=["High-Income Donors", "Low-Income Patients", "NUCLIREGEN Therapies", "Donation Mechanism"],
        color=["#00f7ff", "#ffcf00", "#7efff5", "#fc46aa"]
    ),
    link=dict(
        source=[0, 0, 3],
        target=[2, 3, 1],
        value=[120, 120, 120],
        color=["#00f7ff", "#fc46aa", "#ffcf00"]
    )
))

flow_fig.update_layout(
    title_text="🔄 Global Distribution Model: NUCLIREGEN-P Solidarity System",
    font=dict(size=14, color="white"),
    height=550,
    template="plotly_dark"
)

st.plotly_chart(flow_fig, use_container_width=True)

# Footer
st.markdown("""
    <hr style='border: 1px solid #00ffff;'>
    <p style='text-align: center; color: #aaa;'>NUCLIREGEN-P | Redefining Biomedical Access & Justice 🌐</p>
""", unsafe_allow_html=True)
