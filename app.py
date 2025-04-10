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

st.title("🌍 NUCLIREGEN-P: Global 3D Dashboard")

# ---------- Mapa Interactivo Mundial 3D ----------
st.subheader("🌐 3D Choropleth: Progeria Prevalence & Therapy Access")
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
    color_continuous_scale=px.colors.sequential.Plasma,
    title="Estimated Prevalence of Progeria & Access",
    labels={'Estimated Prevalence': 'Cases'},
    template="plotly_dark",
    projection="orthographic"
)
fig_map.update_geos(showframe=False, showcoastlines=True, projection_scale=0.95)
fig_map.update_layout(height=600, margin=dict(l=0, r=0, t=50, b=0))

st.plotly_chart(fig_map, use_container_width=True)

# ---------- Gráfico de barras: Costo por paciente ----------
st.subheader("💰 3D Bar Chart: Cost per Patient")
cost_df = pd.DataFrame({
    "Therapy": ["NUCLIREGEN-P", "Lonafarnib", "CRISPR"],
    "Cost (USD)": [8000, 100000, 500000]
})

bar_fig = go.Figure(data=[
    go.Bar3d(
        x=cost_df["Therapy"],
        y=["Treatment"] * len(cost_df),
        z=[0]*len(cost_df),
        dx=[0.6]*len(cost_df),
        dy=[0.6]*len(cost_df),
        dz=cost_df["Cost (USD)"],
        text=cost_df["Cost (USD)"],
        hoverinfo='text',
        marker=dict(color=[8000, 100000, 500000], colorscale='Bluered', opacity=0.9)
    )
])
bar_fig.update_layout(
    title="Cost per Therapy (3D Visualization)",
    scene=dict(
        xaxis_title='Therapy',
        yaxis_title='',
        zaxis_title='Cost (USD)',
        bgcolor='#0d1117',
        xaxis=dict(color='white'),
        yaxis=dict(color='white'),
        zaxis=dict(color='white')
    ),
    margin=dict(l=0, r=0, t=50, b=0),
    template="plotly_dark"
)

st.plotly_chart(bar_fig, use_container_width=True)

# ---------- Flujo de distribución solidaria ultra avanzado ----------
st.subheader("🔁 Advanced Sankey Flow: One-for-One Distribution")
flow_fig = go.Figure(go.Sankey(
    arrangement = "snap",
    node = dict(
      pad = 20,
      thickness = 30,
      line = dict(color = "#444", width = 0.5),
      label = ["Global North", "Donation Pipeline", "NUCLIREGEN-P Units", "Global South"],
      color = ["#04f9ff", "#fa00ff", "#00ff6e", "#ffd000"]
    ),
    link = dict(
      source = [0, 1, 2],
      target = [1, 2, 3],
      value = [100, 100, 100],
      color = ["#00f9ff", "#fa00ff", "#00ff6e"]
    )
))
flow_fig.update_layout(
    title_text="Ultra-Detailed Solidarity Distribution Flow",
    font=dict(color="white", size=13),
    height=500,
    paper_bgcolor='#0d1117'
)

st.plotly_chart(flow_fig, use_container_width=True)

# ---------- Footer ----------
st.markdown("""
    <hr style='border: 1px solid #00ffff;'>
    <p style='text-align: center; color: #bbb;'>NUCLIREGEN-P: A Vision of Global Health Equity & Biomedical Precision</p>
""", unsafe_allow_html=True)
