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
    # Curva de cable
    x = np.linspace(0, distancia, 100)
    z_flecha = -4 * flecha / (distancia ** 2) * (x - distancia / 2) ** 2 + flecha
    z_cable = altura_poste - z_flecha
    y = np.zeros_like(x)

    # Coordenadas para flecha roja
    x_flecha = [distancia / 2, distancia / 2]
    y_flecha = [0, 0]
    z_flecha_line = [altura_poste, altura_poste - flecha]
    texto_z = altura_poste + 1.5

    fig = go.Figure()

    # Postes (gruesos)
    fig.add_trace(go.Scatter3d(x=[0, 0], y=[0, 0], z=[0, altura_poste],
                               mode='lines', line=dict(color='saddlebrown', width=16), name='Poste A'))
    fig.add_trace(go.Scatter3d(x=[distancia, distancia], y=[0, 0], z=[0, altura_poste],
                               mode='lines', line=dict(color='saddlebrown', width=16), name='Poste B'))

    # Etiquetas "Poste A" y "Poste B"
    fig.add_trace(go.Scatter3d(x=[0], y=[0], z=[altura_poste + 0.5],
                               mode='text', text=["Poste A"], textfont=dict(size=14), showlegend=False))
    fig.add_trace(go.Scatter3d(x=[distancia], y=[0], z=[altura_poste + 0.5],
                               mode='text', text=["Poste B"], textfont=dict(size=14), showlegend=False))

    # Cable
    fig.add_trace(go.Scatter3d(x=x, y=y, z=z_cable,
                               mode='lines', line=dict(color='gray', width=6), name='Cable'))

    # Flecha vertical roja
    fig.add_trace(go.Scatter3d(x=x_flecha, y=y_flecha, z=z_flecha_line,
                               mode='lines+markers', line=dict(color='red', width=5, dash="dot"),
                               marker=dict(size=4, color='red'), name='Flecha'))

    # Texto de flecha arriba
    fig.add_trace(go.Scatter3d(
        x=[distancia / 2], y=[0], z=[texto_z],
        mode='text',
        text=[f"<b>Flecha = {flecha:.2f} m</b>"],
        textfont=dict(size=16, color='red'),
        showlegend=False
    ))

    # Leyenda lateral informativa (como anotación)
    fig.add_annotation(
        dict(
            showarrow=False,
            text=f"<b>📏 Distancia: {distancia:.1f} m<br>⬇️ Flecha: {flecha:.2f} m<br>📐 Altura poste: {altura_poste:.1f} m</b>",
            xref="paper", yref="paper",
            x=1.02, y=1.0,
            align="left",
            font=dict(size=13),
            bordercolor="black",
            borderwidth=1,
            bgcolor="white",
            opacity=0.9
        )
    )

    # Configuración visual limpia
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
