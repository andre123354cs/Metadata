import streamlit as st
import pandas as pd
import locale
import pyarrow.parquet as pq
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import pyrebase

st.set_page_config(
    page_title="MetaData",
    page_icon=":chart_with_upwards_trend:",
    layout="wide",
    initial_sidebar_state="collapsed"
    )


def interfaz():
    
    locale.setlocale(locale.LC_ALL, 'es_ES')
    locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8') 
    

    # Función para limpiar el caché
    def clear_cache():
        st.cache_data.clear()  # Limpiar el caché de los datos
    
    # Botón para ejecutar la limpieza del caché
    if st.button('Actualizar'):
        clear_cache()
        st.success('¡Actualizado con éxito!')

    
    st.markdown("""
    <h1 style='text-align: center; color: #005780; font-size: 15px;'>Nuestro desarrollo de software está transformando la forma en que trabajamos. Al automatizar tareas repetitivas, liberamos tiempo y recursos para que puedas concentrarte en lo que realmente importa.🖥</h1>
    """, unsafe_allow_html=True)
    
    url_carteras = {
        "Comfama": r"https://drive.usercontent.google.com/u/0/uc?id=1ZBk8wgXGnyTGZKQxNQEmRTmpzTlqa9KO&export=download",
        "Azzorti": r"https://drive.usercontent.google.com/u/0/uc?id=1kxVQ7PvD9ueO8qqZdk9aZotYGVjiRq0Y&export=download",
        "Cueros": r"https://drive.usercontent.google.com/u/0/uc?id=1ffZu1qoNK5iBo7lSo8WbS1bKZRYaIbMK&export=download",
        "Keypagos" : r"https://drive.usercontent.google.com/u/0/uc?id=1zYX2uONwvxBolHPEl4pm3qVjFeTRXCrQ&export=download",
        "Linea Directa": r"https://drive.usercontent.google.com/u/0/uc?id=1ceYiVkmia5GvS1m0TYuv9tdQ00UjhP1A&export=download",
        "Nova Mexico": r"https://drive.usercontent.google.com/u/0/uc?id=1Z8UOXpetXRvDPala0rSzPlQh8tSwbvIA&export=download",
        "Nova_Colombia": r"https://drive.usercontent.google.com/u/0/uc?id=1EkGd1UbyuVpCK2yqDjrxzV1i6SLNi607&export=download",
        #"Dolce": r"https://drive.usercontent.google.com/u/0/uc?id=1Ew7xK8rjDGDA4jjkhQ_XGRfDuFzIG5e8&export=download",
    }

    url_Envios = {
        #"Comfama": r"C:\\Users\\felip\\OneDrive\\Documentos\\Matris\\Comfamax23.parquet",
        "Azzorti": r"https://drive.usercontent.google.com/u/0/uc?id=1EHU0icWd21FjidpFV0dvqnOGujKOHURV&export=download",
        "Cueros": r"https://drive.usercontent.google.com/u/0/uc?id=1flyRur6IcwmNEJvOF0H6X85jxMOarccn&export=download",
        "Keypagos" : r"https://drive.usercontent.google.com/u/0/uc?id=17qzw2bVgnCarY4Q72GT-TlggCkMMbFP4&export=download",
        "Linea Directa": r"https://drive.usercontent.google.com/u/0/uc?id=1--px3G3Q24pF4KaLJKcMvuBTl4dB9aZi&export=download",
        "Nova Mexico": r"https://drive.usercontent.google.com/u/0/uc?id=1iPcptWrVq27AwIXQ2mtDsPJ1IrfVoOWw&export=download",
        "Nova_Colombia": r"https://drive.usercontent.google.com/u/0/uc?id=1hi8FvTIp3WzQh6sY4HOnuRiPuwtJoGnE&export=download",
    }
    
    Pagos_Cruzados = {
        "Comfama": r"https://drive.usercontent.google.com/u/0/uc?id=1u5LH75bdQ5AhJAi67uFfA40EtpANPFNs&export=download",
        "Azzorti": r"https://drive.usercontent.google.com/u/0/uc?id=1R1f6PWmaag4Gm9TGjM_z-EuSz2OEIpQV&export=download",
        "Cueros": r"https://drive.usercontent.google.com/u/0/uc?id=1aBkcFKmqPbJVTZvoUuQGymsUuYWHtyQQ&export=download",
        "Keypago" : r"https://drive.usercontent.google.com/u/0/uc?id=17CSMaLPPY1pOa7_ZykXzvQfhRbPNbGHh&export=download",
        "Linea Directa": r"https://drive.usercontent.google.com/u/0/uc?id=1ityd0ukmDHOvbZfExIldjucF56L-oJS5&export=download",
        "Nova Mexico": r"https://drive.usercontent.google.com/u/0/uc?id=17Mv66TRBPDOHqAAh170PjlRenJaDASd6&export=download",
        "Nova Colombia": r"https://drive.usercontent.google.com/u/0/uc?id=1sSZN5nMI7XTULgiiHFffpr72xMmS712A&export=download",
    }
    
    
    info_carteras = {
        "Comfama": ['Saldo_Total_CO'],
        "Azzorti": ['Saldo_Documento_AZ'],
        "Cueros": ['Valor_saldo_total_créditos_CU'],
        "Keypago" : ['Saldo_Total_a_Hoy_key'],
        "Linea Directa": ['Saldo Total_LD'],
        "Nova Mexico": ['Balance_Estimado_MX'],
        "Nova Colombia": ['Balance_Estimado_COl'],
    }
    
    Fechas_Creacion = {
        "Comfama": ['Fecha_Creacion__CO'],
        "Azzorti": ['Fecha_Creación_AZ'],
        "Cueros": ['Fecha_Creación__CU'],
        "Keypagos" : ['Fecha_Creación__key'],
        "Linea Directa": ['Fecha_Creación__LD'],
        "Nova Mexico": ['Fecha_Creacion__MX'],
        "Nova_Colombia": ['Fecha_Creacion__COl'],
        #"Dolce": ['Fecha Factura']
    }
    columnas_comunes = {
        "Comfama": ['Buscador'],
        "Azzorti": ['Buscador'],
        "Cueros": ['Buscador'],
        "Keypago" : ['Buscador'],
        "Linea Directa": ['Buscador'],
        "Nova Mexico": ['Buscador'],
        "Nova Colombia": ['Buscador'],
    }
    meses = {
        1: 'Enero',
        2: 'Febrero',
        3: 'Marzo',
        4: 'Abril',
        5: 'Mayo',
        6: 'Junio',
        7: 'Julio',
        8: 'Agosto',
        9: 'Septiembre',
        10: 'Octubre',
        11: 'Noviembre',
        12: 'Diciembre',
        1.0: 'Enero',
        2.0: 'Febrero',
        3.0: 'Marzo',
        4.0: 'Abril',
        5.0: 'Mayo',
        6.0: 'Junio',
        7.0: 'Julio',
        8.0: 'Agosto',
        9.0: 'Septiembre',
        10.0: 'Octubre',
        11.0: 'Noviembre',
        12.0: 'Diciembre'
    }
    
    
    colores = {
        1: dict(color='rgb(0, 102, 204)', width=2),    # Azul (intenso)
        2: dict(color='rgb(255, 0, 0)', width=3),      # Rojo (intenso)
        3: dict(color='rgb(0, 204, 0)', width=1),      # Verde (intenso)
        4: dict(color='rgb(255, 140, 0)', width=1),    # Naranja (intenso)
        5: dict(color='rgb(128, 0, 128)', width=1),    # Púrpura (intenso)
        6: dict(color='rgb(255, 99, 71)', width=1),    # Tomate (intenso)
        7: dict(color='rgb(0, 255, 255)', width=1),    # Cian (intenso)
        8: dict(color='rgb(255, 20, 147)', width=1),   # Deep Pink (intenso)
        9: dict(color='rgb(0, 255, 0)', width=1),      # Verde Limón (intenso)
        10: dict(color='rgb(0, 100, 255)', width=1),   # Aqua (intenso)
        11: dict(color='rgb(255, 165, 0)', width=1),   # Naranja (claro)
        12: dict(color='rgb(75, 0, 130)', width=1)     # Índigo (intenso)
    }
    
    
    
    color_map = {
        1: 'rgba(0, 102, 204, 0.4)',    # Azul (intenso) con 40% de transparencia
        2: 'rgba(255, 0, 0, 0.4)',      # Rojo (intenso) con 40% de transparencia
        3: 'rgba(0, 204, 0, 0.4)',      # Verde (intenso) con 40% de transparencia
        4: 'rgba(255, 140, 0, 0.4)',    # Naranja (intenso) con 40% de transparencia
        5: 'rgba(128, 0, 128, 0.4)',    # Púrpura (intenso) con 40% de transparencia
        6: 'rgba(255, 99, 71, 0.4)',    # Tomate (intenso) con 40% de transparencia
        7: 'rgba(0, 255, 255, 0.4)',    # Cian (intenso) con 40% de transparencia
        8: 'rgba(255, 20, 147, 0.4)',   # Deep Pink (intenso) con 40% de transparencia
        9: 'rgba(0, 255, 0, 0.4)',      # Verde Limón (intenso) con 40% de transparencia
        10: 'rgba(0, 100, 255, 0.4)',   # Aqua (intenso) con 40% de transparencia
        11: 'rgba(255, 165, 0, 0.4)',   # Naranja (claro) con 40% de transparencia
        12: 'rgba(75, 0, 130, 0.4)'     # Índigo (intenso) con 40% de transparencia
    }
    
    columnas_por_cartera = {
        "Comfama":["Descripcion_Traslado_CO","Tipo"],
        "Azzorti": ["Codigo_Campana_AZ", "Etapa_AZ", "Efecto_AZ"],
        "Cueros": ["Ano Castigo","Efecto", "Mejor_Efecto","Tipo"], #agregar año de castigo a partir de la fecha actualizacion
        "Keypagos" : ["Franja","Efecto", "Mejor_Efecto","Tipo"],
        "Linea Directa": ["Codigo de la Empresa_LD", "Ano Castigo_LD", "Franja", "Efecto", "Mejor_Efecto","Tipo","Franja"], 
        "Nova Mexico": ["Segmento_MX","Detalle","Mejor_Efecto", "Efecto"],
        "Nova_Colombia": ["Segmento_COl" ,"Numero_Traslado_COl", "Descripcion_Region_COl"]
    
    }
    
    @st.cache_data(ttl=3600, show_spinner=True, persist=True)
    def cargar_parquet(url):
    
        return pd.read_parquet(url)
    
    def generar_grafica_resumen(cartera, mes):
        
        df = cargar_parquet("https://drive.usercontent.google.com/u/0/uc?id=1aZ43gR3A9KmOatn7dNBR5DJvppD-_z_g&export=download")
        df = df[df['Cartera'] == cartera]
        df = df[df['Dia'] >= 1]
    
        mes = df['Mes_Creacion'].unique()
    
        mes = st.segmented_control(
            "Selecciona el mes", sorted(mes), selection_mode="multi", default= mes[-2:]
        )
        
        # Crear la figura base
        fig = go.Figure()
        
        for me in mes:
            grafica = df[df['Mes_Creacion'] == me]
            grafica['valor_acumulado'] = grafica['Aportes'].cumsum()
            grafica = grafica[grafica['valor_acumulado'] > 0.1]        
            if not grafica.empty: 
                ultimo_dia = grafica.iloc[-1]  
                etiqueta = locale.currency(ultimo_dia['valor_acumulado'], grouping=True).split(",")[0]
                fig.add_trace(go.Scatter(
                    x=grafica['Dia'], 
                    y=grafica['valor_acumulado'],
                    mode='lines+text',
                    name=meses[me],
                    line=colores[me],
                    hovertemplate='Día: %{x}<br>Pago: %{y:$,.2f}'
                ))
                fig.add_annotation(
                    x=ultimo_dia['Dia'],
                    y=ultimo_dia['valor_acumulado'],
                    text=f"{etiqueta}",
                    showarrow=True,
                    arrowhead=1,
                    arrowsize=0.5,
                    arrowwidth=0.5,
                    font=dict(size=12, color="black"),
                    bgcolor=color_map[me]
                )
    
        # Configurar el layout de la gráfica
        fig.update_layout(
            title=f'Pagos {cartera}',
            xaxis_title="Día de Pago",
            yaxis_title="Valor Acumulado de Pagos",
            legend_title="Meses",
            hovermode="x unified"
            
        )
    
        return fig
    
    
    
    tab1, tab2, tab3, tab4, tab5, tab6= st.tabs(["Panel de Control 🧮", "Actualizaciones 🗂️",'Consulta 🔍','Envios 📤','-','-'])
    
    with tab1:
        
        st.markdown("""
    <h1 style='text-align: left; color: #005780; font-size: 24px;'>Salud Financiera 📈</h1>
    """, unsafe_allow_html=True)
        
        df = cargar_parquet("https://drive.usercontent.google.com/u/0/uc?id=1GKZz0tGALNjT7p66Pyg-cE2ysomgZXAP&export=download")
    
        meses_unicos = df['Mes_Creacion'].unique()
        meses_filtrados = {k: v for k, v in meses.items() if k in meses_unicos}
    
        meses_ordenados = list(meses_filtrados.values())
        meses_ordenados.sort()
    
        mes_seleccionado = st.selectbox('Selecciona un mes', meses_ordenados, format_func=lambda x: f"{x}")
    
        df_filtrado = df[df['Mes_Creacion'] == list(meses_filtrados.keys())[list(meses_filtrados.values()).index(mes_seleccionado)]]
    
        
        columnas_ocultas = ['Mes_Creacion']
        st.dataframe(df_filtrado.drop(columnas_ocultas, axis=1), use_container_width=True, hide_index=True)
    
    
        st.markdown("""
    <h1 style='text-align: left; color: #005780; font-size: 24px;'>Grafica Comparativa Por Cartera 📊</h1>
    """, unsafe_allow_html=True)
        cartera = st.selectbox('Selecciona una cartera:',list(url_carteras.keys()))
    
        st.plotly_chart(generar_grafica_resumen(cartera,meses_unicos))
    
    
    with tab2:
    
        with st.expander("Actualizaciones 💻"):
            tab54, tab55= st.tabs(["Descargar 📥","-"])
            with tab54: 
                    
                def cargar_parquet(ruta):
                    # Función para cargar un archivo Parquet
                    return pd.read_parquet(ruta)
    
               
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
    
        with st.expander("Pagos 💰"):
            tab1, tab2 = st.tabs(["Descargar 📥", "-"])
            with tab1:
                
                def cargar_y_filtrar_datos(cartera_seleccionada, mes_creacion_filtro):
                    df = cargar_parquet(Pagos_Cruzados[cartera_seleccionada])
                    
                    df_filtrado = df[df['Mes_Creacion'] == mes_creacion_filtro]
                    
                    return df_filtrado
                
                cartera_seleccionadass = st.selectbox("Selecciona una Cartera:  ", list(Pagos_Cruzados.keys()))
                
                if cartera_seleccionadass:
                    df = cargar_parquet(Pagos_Cruzados[cartera_seleccionadass])
                    df['Mes_Creacion'] = df['Mes_Creacion'].astype(int)
                    meses_unicos = df['Mes_Creacion'].unique()
    
    
                    
    
                    mes_creacion_filtro = st.selectbox("Selecciona Mes:  ", meses_unicos)
                
                    df_filtrado = cargar_y_filtrar_datos(cartera_seleccionadass, mes_creacion_filtro)
                    
                    # Calcular la suma de la columna de pagos y el número de registros
                    suma_pagos = df_filtrado['Pagos'].sum()
                    num_registros = len(df_filtrado['Pagos'])
                
                    # Mostrar las etiquetas con la suma y el número de registros
                    st.write(f"La suma total de pagos: ${suma_pagos:,.2f}")
                    st.write(f"El número total de registros: {num_registros}")
    
                    csv = df.to_csv(index=False)
                    st.download_button(
                    label= f"Descargar Pagos De {cartera_seleccionadass}",
                    data=csv,
                    file_name= f"Pagos_{cartera_seleccionadass}_Mes_{mes_creacion_filtro}.csv",
                    mime='text/csv')
                    
    
        with st.expander("Cargue ABC 🔑"):
            tab1, tab2  = st.tabs(["Actializacion 📥", "Demograficos 💻"])
            with tab1:
                
                ruta_csv = "https://drive.usercontent.google.com/u/0/uc?id=1PnBfaYfe9mmpphSuKDPje1zwLj4c-qq5&export=download"
                df = pd.read_csv(ruta_csv, dtype='object')
    
                productos_unicos = df['PRODUCTO'].unique()
    
                productos_seleccionados = st.selectbox('Selecciona Una Cartera:            ', productos_unicos)
                df_filtrado = df[df['PRODUCTO'] == productos_seleccionados]
    
                
                num_registros = len(df_filtrado['PRODUCTO'])
                st.write(f"El número total de registros: {num_registros:,.0f}")
                
                csv = df_filtrado.to_csv(index=False)
                st.download_button(
                label= f"Descargar cargue ABC {productos_seleccionados}",
                data=csv,
                file_name= f"Actualizacion_ABC_{productos_seleccionados}.csv",
                mime='text/csv')
    
            with tab2:
                
                ruta_archivo = "https://drive.usercontent.google.com/u/0/uc?id=1Zrv7iciZtquzFgQb5Qr3Zyaax3rfPTNG&export=download"
                df = cargar_parquet(ruta_archivo)
            
                productos_unicos = df['Cartera'].unique()
            
                productos_seleccionados = st.selectbox('Selecciona Alguna Cartera:', productos_unicos)
                df_filtrado = df[df['Cartera'] == productos_seleccionados]
            
                
                num_registros = len(df_filtrado['Cartera'])
                st.write(f"El número total de registros: {num_registros:,.0f}")
                
                csv = df_filtrado.to_csv(index=False)
                st.download_button(
                label= f"Descargar Demograficos ABC {productos_seleccionados}",
                data=csv,
                file_name= f"Demograficos_{productos_seleccionados}.csv",
                mime='text/csv')
    
        
    
    with tab3:
        with st.expander("Extraer Con Archivo de Cedulas (Base de Datos YESBPO) 💻"):
            tab1, tab2, tab3 = st.tabs(["Descargar 📥", "-","-"])
            with tab1:
                st.markdown("""
    <h1 style='text-align: left; color: #005780; font-size: 24px;'>Mineria de Datos</h1>
    """, unsafe_allow_html=True)
                estructura = pd.DataFrame(columns=['Cedula'])
                csv = estructura.to_csv(index=False)
                st.download_button(
                            label="Descargar Estructura ",
                            data=csv,
                            file_name='Estructura.csv',
                            mime='text/csv',
                        )
                
                # Subida del archivo
                uploaded_file = st.file_uploader("Sube tu archivo CSV ", type=["csv"])
                
                if uploaded_file is not None:
                    # Leer el archivo CSV
                    df = pd.read_csv(uploaded_file)
            
                
        
                ruta_archivo = "https://drive.usercontent.google.com/u/0/uc?id=1cY4ZmU0Bc4FfB4SotOYqCdk9V3JSz4Ok&export=download"
                Demografico = pd.read_csv(ruta_archivo)
            
                #ruta_archivo = "C:\\Users\\felip\\OneDrive\\Documentos\\Matris\\ABC.parquet"
                #Demografico = pq.read_table(ruta_archivo).to_pandas()
            
                Demografico = Demografico.rename(columns={'CEDULA': 'Cedula'})
            
                Resultado = pd.merge( df, Demografico, on='Cedula', how='left')        
                # Mostrar los resultados en un dataframe
            
                # Descargar los resultados como CSV
                if Resultado.empty:
                    st.write("No se encontraron datos para la cédula ingresada. ")
                else:
                    csv = Resultado.to_csv(index=False)
                    st.download_button(
                        label="Descargar Resultados YesBPO ",
                        data=csv,
                        file_name='Resultados.csv',
                        mime='text/csv',
                    )
        
     #_________________________________________________________________________________
        
        with st.expander("Extraer Con Archivo de Cedulas (Base de ABC) 🚦"):
            tab1, tab2, tab3 = st.tabs(["Descargar 📥", "-","-"])
            with tab1:
                st.markdown("""
    <h1 style='text-align: left; color: #005780; font-size: 24px;'>Mineria de Datos</h1>
    """, unsafe_allow_html=True)
                estructura = pd.DataFrame(columns=['Cedula'])
                csv = estructura.to_csv(index=False)
                st.download_button(
                            label=" Descargar Estructura ",
                            data=csv,
                            file_name='Estructura.csv',
                            mime='text/csv',
                        )
                
                # Subida del archivo
                uploaded_file = st.file_uploader(" Sube tu archivo CSV ", type=["csv"])
                
                if uploaded_file is not None:
                    # Leer el archivo CSV
                    df = pd.read_csv(uploaded_file)
            
                
        
                Demografico = cargar_parquet("https://drive.usercontent.google.com/u/0/uc?id=1GEwpqGB5do9MVwpsXVWVox5A25pRLWf0&export=download")
            
                #ruta_archivo = "C:\\Users\\felip\\OneDrive\\Documentos\\Matris\\ABC.parquet"
                #Demografico = pq.read_table(ruta_archivo).to_pandas()
            
                Demografico = Demografico.rename(columns={'CEDULA': 'Cedula'})
            
                Resultado = pd.merge( df, Demografico, on='Cedula', how='left')        
                # Mostrar los resultados en un dataframe
            
                # Descargar los resultados como CSV
                if Resultado.empty:
                    st.write("No se encontraron datos para la cédula ingresada.  ")
                else:
                    csv = Resultado.to_csv(index=False)
                    st.download_button(
                        label=" Descargar Resultados ABC ",
                        data=csv,
                        file_name=' Resultados.csv',
                        mime='text/csv',
                    )
        
     
    #__________________________________________________________________________________
    
    
    with tab4:
    
        st.markdown("""
    <h1 style='text-align: left; color: #005780; font-size: 24px;'>Motor de Envío Masivo🌐</h1>
    """, unsafe_allow_html=True)
    
        # Selección de la cartera
        cartera_seleccionada = st.selectbox("Carteras:", list(url_Envios.keys()))
    
        if cartera_seleccionada:
            # Cargar los datos
            df = cargar_parquet(url_Envios[cartera_seleccionada])
            # Obtener columnas relevantes y valores únicos
            columnas_a_filtrar = columnas_por_cartera[cartera_seleccionada]
            valores_unicos = {columna: sorted(df[columna].astype(str).unique()) for columna in columnas_a_filtrar}
    
            # Crear formulario de filtros
            with st.form("my_form"):
                submit_button = st.form_submit_button("Filtrar")
                for columna, valores in valores_unicos.items():
                    st.session_state[columna] = st.multiselect(f"Selecciona {columna}:", valores, default=valores)
    
            if submit_button:
                # Construir el filtro dinámicamente
                for columna in columnas_a_filtrar:
                    df_filtrado = df[df[columna].isin(st.session_state[columna])]
                #filtro = [df[columna].isin(st.session_state[columna]) for columna in columnas_a_filtrar]
                #df_filtrado = df[np.all(filtro, axis=0)]
    
                # Mostrar resultados
                st.dataframe(df_filtrado.head(10), hide_index=True, use_container_width=True)
                num_registros = len(df_filtrado)
                st.write(f"El número total de registros: {num_registros:,.0f}")
                # Descargar datos
                csv = df_filtrado.to_csv(index=False).encode('utf-8')
                st.download_button(
                    label="Descargar CSV",
                    data=csv,
                    file_name=f"{cartera_seleccionada}_filtrado.csv",
                    mime='text/csv'
                )
    
                # Visualizaciones (opcional)
                #st.line_chart(df_filtrado['Columna_numerica'])  # Reemplaza 'Columna_numerica' con la columna deseada
st.markdown("""
    <style>
        @keyframes spin {
            0% {
                transform: rotateY(0deg);
            }
            100% {
                transform: rotateY(-360deg);
            }
        }

        .rotating-emoji {
            display: inline-block;
            animation: spin 3s linear infinite;
            transform-origin: center center; /* Rota sobre su propio eje */
            font-size: 50px; /* Tamaño del emoji reducido */
            margin-right: 10px; /* Espacio entre el emoji y el título */
        }

        .emoji-container {
            text-align: center;
            margin-top: 50px;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        .title {
            font-size: 50px;
            color: #005780;
        }
    </style>

    <div class="emoji-container">
        <span class="rotating-emoji">🌐</span>
        <h1 class="title">MetaData Yes BPO</h1>
    </div>
""", unsafe_allow_html=True)
# Configuración Firebase
firebaseConfig = {
    "apiKey": "AIzaSyBUxKlDXnPSeNLKYXzsp3pUxJ8giAwSkMQ",
    "authDomain": "metadata-c090e.firebaseapp.com",
    "databaseURL": "https://metadata-c090e-default-rtdb.firebaseio.com",
    "projectId": "metadata-c090e",
    "storageBucket": "metadata-c090e.appspot.com",
    "messagingSenderId": "954810311523",
    "appId": "1:954810311523:web:a6b0681e4f164b60cba956"
}

firebase = pyrebase.initialize_app(firebaseConfig)
pb_auth = firebase.auth()
db = firebase.database()  # Referencia a la base de datos

#st.markdown("""
 #   <h1 style='text-align: center; color: #005780; font-size: 50px;'>🌍 MetaData Yes BPO</h1>
#""", unsafe_allow_html=True)

if 'user_info' not in st.session_state:
    st.session_state.user_info = None

def main():
    if st.session_state.user_info:
        user_info = st.session_state.user_info
        if user_info['role'] == 'admin':
            with st.sidebar:
                st.markdown(f"### 🏠 Bienvenido, {user_info['name']}!")
                st.markdown(f"Rol: **{user_info['role']}**")
                #st.button("Cerrar sesión", on_click=lambda: st.session_state.update({"user_info": None}))
                tabs = st.tabs(["Crear usuario", "Gestionar usuarios"])
                with tabs[0]:
                    create_user_form()
                with tabs[1]:
                    manage_users_module()    
        st.markdown(f"""
<h1 style='text-align: center; color: #005780; font-size: 15px;'>🌱 Bienvenido, {user_info['name']} </h1>
""", unsafe_allow_html=True)  
        interfaz()
    else:
        st.markdown("")
        form = st.form("login_form")
        form.markdown("<h2 style='text-align: center'>Autenticación</h2>", unsafe_allow_html=True)
        email = form.text_input("Correo")
        password = form.text_input("Contraseña", type="password")
        col1, col2 = form.columns([8, 2])
        
        if col2.form_submit_button("Iniciar Sesión"):
            with st.spinner("Procesando..."):
                try:
                    # Autenticar usuario
                    user = pb_auth.sign_in_with_email_and_password(email, password)
                    user_id = user['localId']
                    
                    # Obtener información adicional de la base de datos
                    user_info = db.child("users").child(user_id).get().val()
                    if user_info:
                        if user_info["habilitado"]:
                            st.session_state.user_info = user_info
                            st.toast(f"✅ ¡Inicio de sesión exitoso, {user_info['name']}! 🎉")
                            st.rerun()  # Recargar para mostrar la información
                        else:
                            st.error("❌ El usuario se encuentra inhabilitado.")
                    else:
                        st.error("No se encontró información del usuario.")
                except Exception as e:
                    error_message = str(e)
                    if "INVALID_PASSWORD" in error_message:
                        st.toast("❌ Contraseña incorrecta. 🔒")
                    elif "EMAIL_NOT_FOUND" in error_message:
                        st.toast("❌ Correo no registrado. 📧")
                    else:
                        st.toast("⚠️ Error inesperado. Intenta nuevamente. ❓")
                        st.write(e)


def register_user(email, password, name, role):
    try:
        user = pb_auth.create_user_with_email_and_password(email, password)
        user_id = user['localId']
        # Guardar información adicional en la base de datos
        db.child("users").child(user_id).set({"name": name, "role": role, "email": email, "habilitado": True})
        st.success(f"✅ Usuario {name} creado exitosamente con rol {role}!")
    except Exception as e:
        st.error(f"❌ Error al crear el usuario: {e}")


def create_user_form():
    """Función para mostrar el formulario de creación de usuario."""
    st.markdown("## Crear usuario")
    with st.form("create_user_form"):
        new_email = st.text_input("Correo del nuevo usuario")
        new_password = st.text_input("Contraseña", type="password")
        new_name = st.text_input("Nombre")
        new_role = st.selectbox("Rol", ["admin", "Director", "Coordinador", "Analista"])
        submitted = st.form_submit_button("Crear Usuario")

        if submitted:
            if new_email and new_password and new_name and new_role:
                register_user(new_email, new_password, new_name, new_role)
            else:
                st.error("❌ Todos los campos son obligatorios.")

def manage_users_module():
    """Módulo para gestionar usuarios (cambiar rol y contraseña)."""
    st.markdown("## Gestión de usuarios")
    users = db.child("users").get().val()

    if not users:
        st.warning("No hay usuarios registrados.")
        return

    user_list = [{"id": user_id, **info} for user_id, info in users.items()]
    selected_user = st.selectbox(
        "Selecciona un usuario",
        options=user_list,
        format_func=lambda user: f"{user['name']} ({user['email']})"
    )

    if selected_user:
        st.markdown(f"### Editar usuario: **{selected_user['name']}**")
        formulario_mod_usuario = st.form("form_editar_usuario")
        habilitado = formulario_mod_usuario.checkbox("Habilitado", value=selected_user['habilitado'])
        new_role = formulario_mod_usuario.selectbox(
            "Nuevo rol",
            options=["admin", "Director", "Coordinador", "Analista"],
            index=["admin", "Director", "Coordinador", "Analista"].index(selected_user['role'])
        )
        new_password = formulario_mod_usuario.text_input("Nueva contraseña (opcional)", type="password")

        if formulario_mod_usuario.form_submit_button("Guardar cambios"):
            try:
                # Actualizar rol en la base de datos
                db.child("users").child(selected_user["id"]).update({"role": new_role, 'habilitado': habilitado})

                # Actualizar contraseña si se proporciona una nueva
                if new_password:
                    pb_auth.update_user(selected_user["id"], password=new_password)

                st.success(f"✅ Usuario {selected_user['name']} actualizado correctamente.")
            except Exception as e:
                st.error(f"❌ Error al actualizar el usuario: {e}")


if __name__ == "__main__":
    main()
   
