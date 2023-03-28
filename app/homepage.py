import streamlit as st

def load_homepage():
    '''
    The Homepage is loaded using markdown.
    '''
    st.markdown('This survey includes data from two panels:')
    st.markdown('1. General population who went shopping at a grocery store in the last month')
    st.markdown('2. Caregiver of a fmaily member over the age of 65 who went shopping at a grocery store in the last month')
    