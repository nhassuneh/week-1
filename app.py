import streamlit as st
from apputil import palindrom, parentheses

st.write(
'''
# Week x: [Title]

Testing our utility functions
'''
)

# Text input for palindrome
word = st.text_input("Enter a word or phrase:")

if word:
    st.write("Is palindrome?:", palindrom(word))

# Text input for parentheses
seq = st.text_input("Enter a parentheses sequence:")

if seq:
    st.write("Is valid parentheses sequence?:", parentheses(seq))