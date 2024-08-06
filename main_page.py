# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 09:34:44 2024

@author: SAIL
"""

import streamlit as st

import home, univariate, bi-variate, ml-model 

# Create a menu
st.sidebar.title("Departmental Collaboration Analysis")

#Home page
home.main()


# Add buttons to navigate between pages

if st.sidebar.button('Univariate Statistics'):
    st.session_state.page = 'univariate'
if st.sidebar.button('Bi-Variate Statistics'):
    st.session_state.page = 'bi-variate'
if st.sidebar.button('Machine Learning Models'):
    st.session_state.page = 'ml-models'
    
    

# Display the selected page
if st.session_state.get('page') == 'univariate':
    univariate.main()
elif st.session_state.get('page') == 'bi-variate':
    bi-variate.main()
elif st.session_state.get('page') == 'ml-models':
    ml-models.main()
