# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 09:34:44 2024

@author: SAIL
"""

import streamlit as st
import home, univariate, bi_variate, ml_models

# Create a menu
st.sidebar.title("Departmental Collaboration Analysis")

# Add buttons to navigate between pages
if st.sidebar.button('Home'):
    st.session_state.page = 'home'
if st.sidebar.button('Univariate Statistics'):
    st.session_state.page = 'univariate'
if st.sidebar.button('Bi-Variate Statistics'):
    st.session_state.page = 'bi_variate'
if st.sidebar.button('Machine Learning Models'):
    st.session_state.page = 'ml_models'

# Display the selected page
if 'page' not in st.session_state:
    st.session_state.page = 'home'
if st.session_state.get('page') == 'home':
    home.main()
elif st.session_state.get('page') == 'univariate':
    univariate.main()
elif st.session_state.get('page') == 'bi_variate':
    bi_variate.main()
elif st.session_state.get('page') == 'ml_models':
    ml_models.main()

