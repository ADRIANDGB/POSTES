import streamlit as st
import numpy as np
import plotly.graph_objs as go

st.set_page_config(page_title="Gráfica 3D - Cable con Flecha", layout="centered")
st.title("🌉 Visualización 3D de Cable entre Postes")

st.markdown("Ingresa los parámetros para generar una visualización 3D de un cable suspendido entre dos postes, incluyendo la flecha máxima.")

# Entradas
distancia = st.number_input("📏 Distancia entre postes (m)", min_value=1.0, value=50.0, step=1.0)
altura_poste = st.number_input("📐 Altura de los postes (m)", min_value=1.0, value=10.0, step=0.5)
flecha = st.number_input("⬇️ Flecha máxima del cable (m)", min_value=0.1, value=2.5, step=0.1)

if st.button("🎯 Generar gráfica 3D"):
    # Datos para curva
    x = np.linspace(0, distancia, 100)
    z_flecha = -4 * flecha / (distancia ** 2) * (x - distancia / 2) ** 2 + flecha
    z_cable = altura_poste - z_flecha
    y = np.zeros_like(x)

    # Flecha visual
    x_flecha = [distancia / 2, distancia / 2]
    y_flecha = [0, 0]
    z_flecha_line = [altura_poste, altura_poste - flecha]
    texto_z = altura_poste + 0.8  # Más arriba del poste

    fig = go.Figure()

    # Postes más gruesos
    fig.add_trace(go.Scatter3d(x=[0, 0], y=[0, 0], z=[0, altura_poste],
                               mode='lines', line=dict(color='saddlebrown', width=16)))
    fig.add_trace(go.Scatter3d(x=[distancia, distancia], y=[0, 0], z=[0, altura_poste],
                               mode='lines', line=dict(color='saddlebrown', width=16)))

    # Cable
    fig.add_trace(go.Scatter3d(x=x, y=y, z=z_cable,
                               mode='lines', line=dict(color='gray', width=6)))

    # Flecha roja vertical
    fig.add_trace(go.Scatter3d(x=x_flecha, y=y_flecha, z=z_flecha_line,
                               mode='lines+markers', line=dict(color='red', width=5, dash="dot"),
                               marker=dict(size=4, color='red')))

    # Texto de flecha más arriba
    fig.add_trace(go.Scatter3d(
        x=[distancia / 2], y=[0], z=[texto_z],
        mode='text',
        text=[f"<b>Flecha = {flecha:.2f} m</b>"],
        textfont=dict(size=16, color='red'),
        showlegend=False
    ))

    # Limpieza de visual
    fig.update_layout(
        title="Cable suspendido entre postes con flecha",
        showlegend=False,
        scene=dict(
            xaxis=dict(visible=False),
            yaxis=dict(visible=False),
            zaxis=dict(visible=False),
            bgcolor='white'
        ),
        margin=dict(l=0, r=0, b=0, t=40),
        paper_bgcolor='white',
        plot_bgcolor='white'
    )

    st.plotly_chart(fig, use_container_width=True)
