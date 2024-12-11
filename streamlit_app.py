import streamlit as st
import pandas as pd

gsheetid='1YIvDyrXcDBuz8-NldwlA8bH7lsi6jf3-'
sheetod='805003045'
url = f'https://docs.google.com/spreadsheets/d/{gsheetid}/export?format=csv&gid={sheetod}&format'
Comfama= pd.read_csv(url)
st.dataframe(Comfama, use_container_width=True)

gsheetid='1EkyTvZWSs5AwXFUAMFbqDRBFwdv_IDIA'
sheetod='970977065'
url = f'https://docs.google.com/spreadsheets/d/{gsheetid}/export?format=csv&gid={sheetod}&format'
LD= pd.read_csv(url)
st.dataframe(LD, use_container_width=True)

gsheetid='1GMOhp7Lcpx8JhSZ0UQAZOeQaUSTIgzOX'
sheetod='492241411'
url = f'https://docs.google.com/spreadsheets/d/{gsheetid}/export?format=csv&gid={sheetod}&format'
Cueroz= pd.read_csv(url)
st.dataframe(Cueroz, use_container_width=True)

gsheetid='1BH5wiZqW8FhWe2skm_1LWw1yDskGlhBy'
sheetod='1026942403'
url = f'https://docs.google.com/spreadsheets/d/{gsheetid}/export?format=csv&gid={sheetod}&format'
Key= pd.read_csv(url)
st.dataframe(Key, use_container_width=True)
