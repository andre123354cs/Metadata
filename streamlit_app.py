import streamlit as st
import pandas as pd
import streamlit as st
import pandas as pd
import locale
import os




gsheetid='1YIvDyrXcDBuz8-NldwlA8bH7lsi6jf3-'
sheetod='805003045'
url = f'https://docs.google.com/spreadsheets/d/{gsheetid}/export?format=csv&gid={sheetod}&format'
Comfama= pd.read_csv(url)

gsheetid='1EkyTvZWSs5AwXFUAMFbqDRBFwdv_IDIA'
sheetod='970977065'
url = f'https://docs.google.com/spreadsheets/d/{gsheetid}/export?format=csv&gid={sheetod}&format'
Directa= pd.read_csv(url)

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



st.markdown("""
<h1 style='text-align: center; color: #005780; font-size: 15px;'>Nuestro desarrollo de software está transformando la forma en que trabajamos. Al automatizar tareas repetitivas, liberamos tiempo y recursos para que puedas concentrarte en lo que realmente importa.🖥</h1>
""", unsafe_allow_html=True)

gsheet_urls = {
    "Comfama": Comfama,
    #"Azzorti": r"C:\\Users\\felip\\OneDrive\\Documentos\\Matris\\Azzorti.parquet",
    "Cueros": Cueroz,
    "Keypagos" : Key,
    "Linea Directa": Directa,
    "Nova Mexico": Mexico,
    "Nova Colombia": Colombia,
    #"Dolce": r"C:\\Users\\felip\\OneDrive\\Documentos\\Matris\\Dolce_Actualizacion.csv",
}


# Definir una función para cargar los datos
def cargar_datos(url):
    return pd.read_csv(url)

# Selección de cartera
cartera_seleccionada = st.selectbox("Selecciona alguna cartera para descargar actualización: ", list(url_carteras.keys()))

if cartera_seleccionada: 
    # Cargar los datos de la cartera seleccionada 
    df = cargar_datos(gsheet_urls[cartera_seleccionada]) 
    # Mostrar los datos en Streamlit 
    st.dataframe(df, use_container_width=True, hide_index=True)

    
