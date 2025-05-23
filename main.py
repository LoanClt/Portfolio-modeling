import streamlit as st

st.title('My First Streamlit App')
st.write('Welcome to your first Streamlit app!')

number = st.slider('Pick a number', 0, 100, 50)
st.write(f'You selected: {number}')
