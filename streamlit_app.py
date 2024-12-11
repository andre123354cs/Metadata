import streamlit as st
import pandas as pd

# URL del archivo CSV en GitHub
url = "https://yesbpo201-my.sharepoint.com/personal/bi_yesbpo201_onmicrosoft_com/Documents/ACTUALIZACION/BD.csv"

# Cargar el archivo CSV
df = pd.read_csv(url)

# Mostrar el contenido del archivo CSV
st.write(df)

