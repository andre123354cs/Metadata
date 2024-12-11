import streamlit as st
import pandas as pd

gsheetid='1YIvDyrXcDBuz8-NldwlA8bH7lsi6jf3-'
sheetod='805003045'
url = f'https://docs.google.com/spreadsheets/d/{gsheetid}/export?format=csv&gid={sheetod}&format'
Comfama= pd.read_csv(url)

gsheetid='1EkyTvZWSs5AwXFUAMFbqDRBFwdv_IDIA'
sheetod='970977065'
url = f'https://docs.google.com/spreadsheets/d/{gsheetid}/export?format=csv&gid={sheetod}&format'
LD= pd.read_csv(url)

gsheetid='1GMOhp7Lcpx8JhSZ0UQAZOeQaUSTIgzOX'
sheetod='492241411'
url = f'https://docs.google.com/spreadsheets/d/{gsheetid}/export?format=csv&gid={sheetod}&format'
Cueroz= pd.read_csv(url)

gsheetid='1BH5wiZqW8FhWe2skm_1LWw1yDskGlhBy'
sheetod='1026942403'
url = f'https://docs.google.com/spreadsheets/d/{gsheetid}/export?format=csv&gid={sheetod}&format'
Key= pd.read_csv(url)

gsheetid='1HFR7b0BbsivMJ_312RbBsEn6zXXz6kOV'
sheetod='771180495'
url = f'https://docs.google.com/spreadsheets/d/{gsheetid}/export?format=csv&gid={sheetod}&format'
Mexico= pd.read_csv(url)

gsheetid='1aFg0IKbjk4uspp1w_1aXmVcjw4AYP7_D'
sheetod='999400508'
url = f'https://docs.google.com/spreadsheets/d/{gsheetid}/export?format=csv&gid={sheetod}&format'
Colombia= pd.read_csv(url)

gsheetid='1hGT-SReZ3HqD-Yc5zMVNzdSpaiRB_sfD'
sheetod='506507018'
url = f'https://docs.google.com/spreadsheets/d/{gsheetid}/export?format=csv&gid={sheetod}&format'
Estimado= pd.read_csv(url)

gsheetid='1x8OPh1Fndy2Lm1fjrWTShvubmytZJBbv'
sheetod='1269902588'
url = f'https://docs.google.com/spreadsheets/d/{gsheetid}/export?format=csv&gid={sheetod}&format'
Pagos= pd.read_csv(url)

gsheetid='1MYqkt0zUIk-I-INyv98r366v93Nxzsfv'
sheetod='2132397615'
url = f'https://docs.google.com/spreadsheets/d/{gsheetid}/export?format=csv&gid={sheetod}&format'
Estractor= pd.read_csv(url)

gsheetid='1HwS85Vk6cn877K9AgjWsrctYqEGSnNT-'
sheetod='1063943345'
url = f'https://docs.google.com/spreadsheets/d/{gsheetid}/export?format=csv&gid={sheetod}&format'
Demos= pd.read_csv(url)


import streamlit as st
import pandas as pd
import locale
import os
import requests
import re
import glob
import pyarrow.parquet as pq
from datetime import datetime
import calendar
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import streamlit_authenticator as stauth


st.markdown("""
<h1 style='text-align: center; color: #005780; font-size: 15px;'>Nuestro desarrollo de software está transformando la forma en que trabajamos. Al automatizar tareas repetitivas, liberamos tiempo y recursos para que puedas concentrarte en lo que realmente importa.🖥</h1>
""", unsafe_allow_html=True)

url_carteras = {
    "Comfama": Comfama,
    #"Azzorti": r"C:\\Users\\felip\\OneDrive\\Documentos\\Matris\\Azzorti.parquet",
    "Cueros": Cueroz,
    "Keypagos" : Key,
    "Linea Directa": LD,
    "Nova Mexico": Mexico,
    "Nova_Colombia": Colombia,
    #"Dolce": r"C:\\Users\\felip\\OneDrive\\Documentos\\Matris\\Dolce_Actualizacion.csv",
}
def cargar_parquet(url):
    return pd.read_excel(url)

cartera_seleccionada = st.selectbox("Selecciona Alguna Cartera para descargar actualizacion: ", list(Fechas_Creacion.keys()))
      
      if cartera_seleccionada:
          # Cargar los datos
          df = cargar_parquet(url_carteras[cartera_seleccionada])
      
          # Obtener la columna de fecha de creación según la cartera
          columna_fecha = Fechas_Creacion[cartera_seleccionada][0]
      
      
    
      # Mostrar el número de clientes activos
      num_registros = len(df['Cartera_x'])
      st.write(f"Clientes Activos: {int(num_registros):,}")
    
      csv = df.to_csv(index=False)
      st.download_button(
      label= f"Descargar Actualizacion De {cartera_seleccionada}",
      data=csv,
      file_name= f"Actualizacion_{cartera_seleccionada}.csv",
      mime='text/csv')
