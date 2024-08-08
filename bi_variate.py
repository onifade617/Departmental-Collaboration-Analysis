# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 09:54:06 2024

@author: SAIL
"""

import streamlit as st


def main():
    st.title("Bivariate")
    
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Communication Patterns During Work Hours",
                                     "Workday Communication Trends",
                                     "Executive Communication During Work Hours", 
                                     "Departmental Communication During Work Hours", 
                                     "Email Sentiment Analysis During Work Hours",
                                     "Device Usage During Work Hours"])

    with tab1:
        st.title("Communication Patterns During Work Hours")
        
        
        
    with tab2:
        st.title("Workday Communication Trends")
    
        
    with tab3:
        st.title("Executive Communication During Work Hours")
        
        
    with tab4:
        st.title("Departmental Communication During Work Hours")
        
        
        
    with tab5:
        st.title("Email Sentiment Analysis During Work Hours")
    
        
    with tab6:
        st.title("Device Usage During Work Hours")
        