import streamlit as st
import numpy as np
import plotly.graph_objs as go

st.set_page_config(page_title="Gráfica 3D - Cable con Flecha", layout="centered")
st.title("🌉 Visualización 3D de Cable entre Postes")

st.markdown("Ingresa los parámetros para generar una visualización 3D de un cable con flecha suspendido entre dos postes.")

# Entradas del usuario
distancia = st.number_input("📏 Distancia entre postes (m)", min_value=1.0, value=50.0, step=1.0)
altura_poste = st.number_input("📐 Altura de los postes (m)", min_value=1.0, value=10.0, step=0.5)
flecha = st.number_input("⬇️ Flecha máxima del cable (m)", min_value=0.1, value=2.5, step=0.1)

if st.button("🎯 Generar gráfica 3D"):
    # Generar coordenadas de la curva (parábola descendente)
    x = np.linspace(0, distancia, 100)
    z_flecha = -4 * flecha / (distancia ** 2) * (x - distancia / 2) ** 2 + flecha  # parábola invertida
    z_cable = altura_poste - z_flecha  # restamos la flecha desde la altura del poste
    y = np.zeros_like(x)

    # Crear figura 3D
    fig = go.Figure()

    # Postes
    fig.add_trace(go.Scatter3d(x=[0, 0], y=[0, 0], z=[0, altura_poste],
                               mode='lines', line=dict(color='saddlebrown', width=10), name='Poste A'))
    fig.add_trace(go.Scatter3d(x=[distancia, distancia], y=[0, 0], z=[0, altura_poste],
                               mode='lines', line=dict(color='saddlebrown', width=10), name='Poste B'))

    # Cable
    fig.add_trace(go.Scatter3d(x=x, y=y, z=z_cable,
                               mode='lines', line=dict(color='gray', width=6), name='Cable'))

    # Configuración
    fig.update_layout(
        title="Cable suspendido entre postes con flecha",
        scene=dict(
            xaxis_title='Distancia (m)',
            yaxis_title='Y (vista lateral)',
            zaxis_title='Altura (m)',
            zaxis=dict(range=[0, altura_poste + 2])
        ),
        margin=dict(l=0, r=0, b=0, t=40)
    )

    st.plotly_chart(fig, use_container_width=True)
