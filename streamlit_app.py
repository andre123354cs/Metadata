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
    def cargar_parquet(url):
    
        return pd.read_parquet(url)
    
    def generar_grafica_resumen(cartera, mes):
        
        df = cargar_parquet("C:\\Users\\felip\\OneDrive\\Documentos\\Matris\\Grafica.parquet")
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
        
        df = cargar_parquet("C:\\Users\\felip\\OneDrive\\Documentos\\Matris\\Tabla_Princi.parquet")
    
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
                
                ruta_csv = "C:\\Users\\felip\\OneDrive\\Documentos\\Matris\\ABC´s\\Archivos_ABC.csv"
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
                
                ruta_archivo = "C:\\Users\\felip\\OneDrive\\Documentos\\Matris\\Demografico.parquet"
                df = pq.read_table(ruta_archivo).to_pandas()
            
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
            
                
        
                ruta_archivo = "C:\\Users\\felip\\OneDrive\\Documentos\\Matris\\Extractor2025.csv"
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
            
                
        
                Demografico = cargar_parquet("C:\\Users\\felip\\OneDrive\\Documentos\\Matris\\Exporta_ABC.parquet")
            
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
                for columna, valores in valores_unicos.items():
                    st.session_state[columna] = st.multiselect(f"Selecciona {columna}:", valores, default=valores)
                submit_button = st.form_submit_button("Filtrar")
    
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
    
