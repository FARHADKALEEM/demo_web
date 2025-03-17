import streamlit as st
name=st.text_input("Enter your name : ")
fname=st.text_input("Enter your father name")
clas=st.selectbox("Enter your class ",(1,2,3,4,5))
hm=st.text_input("enter your contact")
import pandas as pd
# df=pd.read_csv("C:/Users/Hussian computer/Downloads/fraudTest.csv")
# st.dataframe(df)
button=st.button("Done")
if button:
    st.markdown(f"""
    \nname:{name}
    \nfathername :{fname}
    \nclass : {clas}
    contact :{hm}""")