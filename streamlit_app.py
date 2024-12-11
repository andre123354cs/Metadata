import streamlit as st
import pandas as pd

# URL del archivo CSV en GitHub
url = "https://raw.githubusercontent.com/tu_usuario/tu_repositorio/rama/tu_archivo.csv"

# Cargar el archivo CSV
df = pd.read_csv(url)

# Mostrar el contenido del archivo CSV
st.write(df)
