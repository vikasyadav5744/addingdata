import pandas
import streamlit as st
import numpy as np
st.write("addind data to github excel page")
file_name='https://github.com/vikasyadav5744/vikasyadav5744/blob/main/sample.xlsx'
upload=st.file_uploader("csv file upload here")
if upload !=None:
  #master = pd.read_excel(file_name)
  newfile=pd.read_csv(upload, skiprows=1)
  st.write(master)
  st.write(newfile)
else:
  st.write("upload csv")

st.write("Thanks for coding")
