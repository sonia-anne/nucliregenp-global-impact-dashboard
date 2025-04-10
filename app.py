import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="NUCLIREGEN-P | Global & Economic Impact", layout="wide", page_icon="🌍")

# Modo oscuro mejorado + diseño moderno
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
        .css-1v0mbdj p, .css-1v0mbdj span {
            color: #ffffff !important;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🌍 NUCLIREGEN-P: Global Prevalence, Cost & Access Dashboard")

# ---------- Mapa Interactivo Mundial 3D Mejorado ----------
st.subheader("🌡️ 3D Choropleth Map: Global Progeria Prevalence & Access")
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
    color_continuous_scale=px.colors.sequential.Viridis,
    title="Global Prevalence of Progeria and Therapy Access",
    template="plotly_dark",
    projection="natural earth"
)
fig_map.update_geos(showframe=True, showcoastlines=True, showland=True, landcolor="#1f1f2e")
fig_map.update_layout(height=650, margin=dict(l=0, r=0, t=40, b=0))

st.plotly_chart(fig_map, use_container_width=True)

# ---------- Gráfico de barras: Costos por Paciente Mejorado ----------
st.subheader("💸 Cost per Patient: NUCLIREGEN-P vs. Others")
cost_df = pd.DataFrame({
    "Therapy": ["NUCLIREGEN-P", "Lonafarnib", "CRISPR"],
    "Cost (USD)": [8000, 100000, 500000]
})

bar_fig = go.Figure()
bar_fig.add_trace(go.Bar(
    x=cost_df["Therapy"],
    y=cost_df["Cost (USD)"],
    marker_color=["#00ffff", "#ffaa00", "#ff004c"],
    text=cost_df["Cost (USD)"],
    texttemplate="$%{y:,.0f}",
    textposition="outside"
))
bar_fig.update_layout(
    template="plotly_dark",
    title="Comparative Cost per Treatment",
    xaxis_title="Therapy",
    yaxis_title="Cost (USD)",
    height=500,
    margin=dict(l=40, r=40, t=50, b=40),
    plot_bgcolor="rgba(0,0,0,0)",
    paper_bgcolor="rgba(0,0,0,0)"
)

st.plotly_chart(bar_fig, use_container_width=True)

# ---------- Esquema Solidario: Flujo Sankey Mejorado ----------
st.subheader("🔁 One-for-One Donation Flow (Solidarity North-South Model)")
flow_fig = go.Figure(go.Sankey(
    node=dict(
        pad=20,
        thickness=30,
        line=dict(color="#ffffff", width=1),
        label=["High-Income Donors", "Donation System", "NUCLIREGEN Units", "Low-Income Recipients"],
        color=["#00ffff", "#29abe2", "#2df5b0", "#ffaa00"]
    ),
    link=dict(
        source=[0, 0, 1],
        target=[1, 2, 3],
        value=[120, 100, 100],
        color=["#00ffff", "#2df5b0", "#ffaa00"]
    )
))
flow_fig.update_layout(
    title_text="Solidarity Distribution Model: NUCLIREGEN-P Access Equity",
    font_size=14,
    template="plotly_dark",
    height=500,
    margin=dict(l=0, r=0, t=30, b=0)
)

st.plotly_chart(flow_fig, use_container_width=True)

# ---------- Footer ----------
st.markdown("""
    <hr style='border: 1px solid #00ffff;'>
    <p style='text-align: center; color: #aaa;'>Part of NUCLIREGEN-P | Global Health Equity & Precision Medicine Initiative</p>
""", unsafe_allow_html=True)
