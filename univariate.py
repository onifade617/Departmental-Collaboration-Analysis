# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 09:53:18 2024

@author: SAIL
"""

import streamlit as st

def main():
    st.markdown("## Univariate Statistics")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("## Variable 1")
    with col2:
        st.markdown("## Variable 2")
    with col3:
        st.markdown("## Variable 3")

    col4, col5, col6 = st.columns(3)
    with col4:
        st.markdown("## Variable 4")
    with col5:
        st.markdown("## Variable 5")
    with col6:
        st.markdown("## Variable 6")

    col7, col8, col9 = st.columns(3)
    with col7:
        st.markdown("## Variable 7")
    with col8:
        st.markdown("## Variable 8")
    with col9:
        st.markdown("## Variable 9")

