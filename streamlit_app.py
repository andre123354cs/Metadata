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

gsheetid='1HFR7b0BbsivMJ_312RbBsEn6zXXz6kOV'
sheetod='771180495'
url = f'https://docs.google.com/spreadsheets/d/{gsheetid}/export?format=csv&gid={sheetod}&format'
Mexico= pd.read_csv(url)
st.dataframe(Mexico, use_container_width=True)

gsheetid='1aFg0IKbjk4uspp1w_1aXmVcjw4AYP7_D'
sheetod='999400508'
url = f'https://docs.google.com/spreadsheets/d/{gsheetid}/export?format=csv&gid={sheetod}&format'
Colombia= pd.read_csv(url)
st.dataframe(Colombia, use_container_width=True)

gsheetid='1hGT-SReZ3HqD-Yc5zMVNzdSpaiRB_sfD'
sheetod='506507018'
url = f'https://docs.google.com/spreadsheets/d/{gsheetid}/export?format=csv&gid={sheetod}&format'
Estimado= pd.read_csv(url)
st.dataframe(Estimado, use_container_width=True)

gsheetid='1x8OPh1Fndy2Lm1fjrWTShvubmytZJBbv'
sheetod='1269902588'
url = f'https://docs.google.com/spreadsheets/d/{gsheetid}/export?format=csv&gid={sheetod}&format'
Pagos= pd.read_csv(url)
st.dataframe(Pagos, use_container_width=True)

gsheetid='1MYqkt0zUIk-I-INyv98r366v93Nxzsfv'
sheetod='2132397615'
url = f'https://docs.google.com/spreadsheets/d/{gsheetid}/export?format=csv&gid={sheetod}&format'
Estractor= pd.read_csv(url)
st.dataframe(Estractor, use_container_width=True)
