
from pymongo import MongoClient
import pandas as pd
import streamlit as st


st.set_page_config(layout="wide")
st.sidebar.header('selecione o display')

client = MongoClient("localhost", 27017)

db = client.Data_Challenge_Dev

texto = db.texto.find()

dat = pd.DataFrame(texto, columns=['text', 'created_at', 'retweet_count', 'favorite_count'])

dat = dat.fillna(0)

dat["data"] = dat["created_at"].astype("datetime64")

dat["data"] = pd.to_datetime(dat["created_at"], errors="coerce")


st.title("Qual Herói mais comentado")

st.dataframe(dat)






