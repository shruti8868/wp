import streamlit as st
import pickle

st.title("Weather Prediction App")
pn=st.number_input("Enter Precipitation")
maxt=st.number_input("Enter Maximum Temperature")
mint=st.number_input("Enter Minimum Temperature")
wind=st.number_input("Enter Wind Speed")
button=st.button("predict")
if button:
    lr=pickle.load(open("wp.pkl","rb"))
    res=lr.predict([[pn,maxt,mint,wind]])[0]
    st.markdown(f"Today's Weather Situation :{res}")