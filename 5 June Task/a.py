import streamlit as st;
import pandas as pd
import matplotlib as plt

st.title("Election Commission of India")
st.header("Party Wise Result Status")

df = pd.read_csv('Party.csv')
df

plt.pie(df)