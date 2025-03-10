import streamlit as st
import pandas as pd
import requests
import io
import time

def cargar_datos():
    url = "https://powerbi.yesbpo.com/index.php/s/Y3MKBpjYCL2H3wn/download/resultados_whatsapp.xlsx"
    try:
        response = requests.get(url)
        response.raise_for_status()
        excel_file = io.BytesIO(response.content)
        df = pd.read_excel(excel_file)
        return df
    except requests.exceptions.RequestException as e:
        st.error(f"Error al descargar el archivo: {e}")
        return None
    except pd.errors.ParserError as e:
        st.error(f"Error al leer el archivo Excel: {e}")
        return None
    except Exception as e:
        st.error(f"Ocurrió un error inesperado: {e}")
        return None

def app():
    st.title("Resultados de WhatsApp")

    if 'df' not in st.session_state:
        st.session_state.df = cargar_datos()

    if st.session_state.df is not None:
        st.session_state.df['Mensaje'] = st.session_state.df['Mensaje'].replace('MetaData YesBpo', 'Si tienen WhatsApp')
        st.session_state.df['Mensaje'] = st.session_state.df['Mensaje'].apply(lambda x: 'No tienen WhatsApp' if x != 'Si tienen WhatsApp' else x)

        con_whatsapp = st.session_state.df[st.session_state.df['Mensaje'] == 'Si tienen WhatsApp']
        sin_whatsapp = st.session_state.df[st.session_state.df['Mensaje'] == 'No tienen WhatsApp']
        total_numeros = len(st.session_state.df)

        st.markdown(f"<div style='width: 100%; word-wrap: break-word;'>Números con WhatsApp: {len(con_whatsapp)}</div>", unsafe_allow_html=True)
        st.markdown(f"<div style='width: 100%; word-wrap: break-word;'>Números sin WhatsApp: {len(sin_whatsapp)}</div>", unsafe_allow_html=True)
        st.markdown(f"<div style='width: 100%; word-wrap: break-word;'>Total de números validados: {total_numeros}</div>", unsafe_allow_html=True)

        st.write("Tabla de datos:")
        st.dataframe(st.session_state.df)

    time.sleep(5)  # Espera 5 segundos
    st.rerun()  # Recarga la aplicación

if __name__ == "__main__":
    app()
