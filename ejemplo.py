import streamlit as st
import pandas as pd
import plotly.graph_objs as go

st.set_page_config(page_title="Gráfica 3D - Tiempo vs Cantidad", layout="centered")

st.title("📊 Gráfica 3D de Datos Ingresados")

st.markdown("Ingrese manualmente los 5 registros con **Tiempo**, **Cantidad**, y **Valor adicional** (para eje Z).")

# Tabla editable para ingresar los datos
df_input = pd.DataFrame({
    'Tiempo': [0, 0, 0, 0, 0],
    'Cantidad': [0, 0, 0, 0, 0],
    'Valor Adicional (Z)': [0, 0, 0, 0, 0]
})

df = st.data_editor(df_input, num_rows="dynamic", use_container_width=True)

if st.button("📈 Generar Gráfica 3D"):
    if df.shape[0] < 1:
        st.warning("⚠️ Ingresa al menos un registro.")
    else:
        fig = go.Figure(data=[go.Scatter3d(
            x=df['Tiempo'],
            y=df['Cantidad'],
            z=df['Valor Adicional (Z)'],
            mode='markers+lines',
            marker=dict(
                size=6,
                color=df['Valor Adicional (Z)'],
                colorscale='Viridis',
                opacity=0.8
            )
        )])

        fig.update_layout(
            title='Gráfica 3D: Tiempo vs Cantidad vs Valor Adicional',
            scene=dict(
                xaxis_title='Tiempo',
                yaxis_title='Cantidad',
                zaxis_title='Valor Adicional'
            ),
            margin=dict(l=0, r=0, b=0, t=40)
        )

        st.plotly_chart(fig, use_container_width=True)
