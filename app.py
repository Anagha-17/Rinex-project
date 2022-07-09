import streamlit as st
import joblib
model = joblib.load('train')
st.title('song type')            
ip = st.text_input('Enter your song')       
op = model.predict([ip])           
if st.button('Predict'):   
  st.title(op[0]) 

         
