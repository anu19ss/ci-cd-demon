import streamlit as st

st.title("Simple Add App")

a = st.number_input("Enter number A", value=0)
b = st.number_input("Enter number B", value=0)

if st.button("Add"):
    st.success(f"Result: {a + b}")
import streamlit as st

st.title("Simple Add App")

a = st.number_input("Enter number A", value=0)
b = st.number_input("Enter number B", value=0)

if st.button("Add"):
    st.success(f"Result: {a + b}")
