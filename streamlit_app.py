import streamlit as st
import pandas as pd

gsheetid='1YIvDyrXcDBuz8-NldwlA8bH7lsi6jf3'
sheetod='805003045'
url = f'https://docs.google.com/spreadsheets/d/{gsheetid}/export?format=csv&gid={sheetod}&format'

dfDatos= pd.read_csv(url)

