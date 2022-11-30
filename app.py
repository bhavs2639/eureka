import streamlit as st
st.title("Subtraction of two numbers")
A=st.number_input("enter the first number")
B=st.number_input("enter the second number")
C=A-B
st.write("The subtraction answer is",C)

