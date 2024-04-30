import streamlit as st

if st.button('Say hello'):
   st.write('Hello!')
else:
    st.write('Please click the button')

uploaded_file = st.file_uploader("Upload a File Here", type=["csv"])
if uploaded_file is not None:
   st.write('Uploaded')



