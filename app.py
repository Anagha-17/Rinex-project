import streamlit as st
import joblib
model =joblib.load('train.csv')
st.title('PREDICT THE TYPE')
ip=st.text_input('ENTER THE SONG')
op= model.predict([ip])
if st.button('PREDICT'):
 st.title(op[0])
   
