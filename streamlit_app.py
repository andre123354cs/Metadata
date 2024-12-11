import streamlit as st
import pandas as pd
import io

st.set_page_config(
    page_title="MetaData",
    page_icon=":chart_with_upwards_trend:",
    layout="wide",
    initial_sidebar_state="collapsed"
    )

gsheet_urls = {
    "Comfama": 'https://docs.google.com/spreadsheets/d/1YIvDyrXcDBuz8-NldwlA8bH7lsi6jf3-/export?format=csv&gid=805003045',
    "Linea Directa": 'https://docs.google.com/spreadsheets/d/1EkyTvZWSs5AwXFUAMFbqDRBFwdv_IDIA/export?format=csv&gid=970977065',
    "Cueros": 'https://docs.google.com/spreadsheets/d/1GMOhp7Lcpx8JhSZ0UQAZOeQaUSTIgzOX/export?format=csv&gid=492241411',
    "Keypagos": 'https://docs.google.com/spreadsheets/d/1BH5wiZqW8FhWe2skm_1LWw1yDskGlhBy/export?format=csv&gid=1026942403',
    "Nova Mexico": 'https://docs.google.com/spreadsheets/d/1HFR7b0BbsivMJ_312RbBsEn6zXXz6kOV/export?format=csv&gid=771180495',
    "Nova Colombia": 'https://docs.google.com/spreadsheets/d/1aFg0IKbjk4uspp1w_1aXmVcjw4AYP7_D/export?format=csv&gid=999400508',
    "Estimado": 'https://docs.google.com/spreadsheets/d/1hGT-SReZ3HqD-Yc5zMVNzdSpaiRB_sfD/export?format=csv&gid=506507018',
    "Pagos": 'https://docs.google.com/spreadsheets/d/1x8OPh1Fndy2Lm1fjrWTShvubmytZJBbv/export?format=csv&gid=1269902588',
    "Estractor": 'https://docs.google.com/spreadsheets/d/1MYqkt0zUIk-I-INyv98r366v93Nxzsfv/export?format=csv&gid=2132397615',
    "Demos": 'https://docs.google.com/spreadsheets/d/1HwS85Vk6cn877K9AgjWsrctYqEGSnNT-/export?format=csv&gid=1063943345'
}

@st.cache_data(ttl=3600, show_spinner=True, persist=True)
def cargar_datos(url):
    return pd.read_csv(url)

# Título de la aplicación en Streamlit
st.markdown("""
<h1 style='text-align: center; color: #005780; font-size: 15px;'>Nuestro desarrollo de software está transformando la forma en que trabajamos. Al automatizar tareas repetitivas, liberamos tiempo y recursos para que puedas concentrarte en lo que realmente importa.🖥</h1>
""", unsafe_allow_html=True)

# Selección de cartera
cartera_seleccionada = st.selectbox("Selecciona alguna cartera para descargar actualización: ", list(gsheet_urls.keys()))

if cartera_seleccionada:
    # Cargar los datos de la cartera seleccionada
    df = cargar_datos(gsheet_urls[cartera_seleccionada])

    # Mostrar los datos en Streamlit
    st.dataframe(df, use_container_width=True, hide_index=True)

    # Crear un botón de descarga para el archivo completo
    csv = df.to_csv(index=False)
    b = io.BytesIO()
    b.write(csv.encode())
    b.seek(0)

    st.download_button(
        label="Descargar datos completos como CSV",
        data=b,
        file_name='datos_completos.csv',
        mime='text/csv'
    )
