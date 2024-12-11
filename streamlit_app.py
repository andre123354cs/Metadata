import streamlit as st
import pandas as pd

# URL del archivo CSV en GitHub
url = "https://yesbpo201-my.sharepoint.com/:x:/g/personal/bi_yesbpo201_onmicrosoft_com/ESYDoH4rPDJLtaICGzphM98BXa_lqjTBjMUxSixhmbp9Cg?e=Sz5INZ"

# Cargar el archivo CSV
df = pd.read_csv(url)

# Mostrar el contenido del archivo CSV
st.write(df)

