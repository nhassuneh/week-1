import streamlit as st
from apputil import palindrom, parentheses

st.write(
'''
# Week 1: Palindrome Detector & Parentheses Validator

Testing our utility functions
'''
)

# Text input for palindrome
st.subheader("Palindrome Detector")
word = st.text_input("Enter a word or phrase:")

if word:
    st.write("Is palindrome?:", palindrom(word))

# Text input for parentheses
st.subheader("Parentheses Validator")
seq = st.text_input("Enter a parentheses sequence:")

if seq:
    st.write("Is valid parentheses sequence?:", parentheses(seq))