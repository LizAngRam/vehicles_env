import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="Análisis de vehículos",
    layout="wide"
)

st.title("Análisis de anuncios de vehículos")
st.markdown("Visualización interactiva de datos de vehículos usados")

car_data = pd.read_excel('vehicles_us.xlsx')

st.subheader("Vista previa del dataset")
st.dataframe(car_data.head())

numeric_columns = [
    'price',
    'model_year',
    'odometer',
    'days_listed'
]

build_histogram = st.checkbox("Mostrar histograma")
build_scatter = st.checkbox("Mostrar gráfico de dispersión")

if build_histogram:
    st.subheader("Histograma")

    hist_column = st.selectbox(
        "Selecciona la columna para el histograma:",
        numeric_columns
    )

    st.write(f"Distribución de {hist_column}")

    fig_hist = px.histogram(
        car_data,
        x=hist_column,
        title=f"Distribución de {hist_column}"
    )

    st.plotly_chart(fig_hist, use_container_width=True)

if build_scatter:
    st.subheader("Gráfico de dispersión")

    x_axis = st.selectbox(
        "Selecciona el eje X:",
        numeric_columns,
        index=2
    )

    y_axis = st.selectbox(
        "Selecciona el eje Y:",
        numeric_columns,
        index=0
    )

    st.write(f"Relación entre {x_axis} y {y_axis}")

    fig_scatter = px.scatter(
        car_data,
        x=x_axis,
        y=y_axis,
        title=f"{y_axis} vs {x_axis}",
        opacity=0.6
    )

    st.plotly_chart(fig_scatter, use_container_width=True)
