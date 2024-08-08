# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 09:53:18 2024

@author: SAIL
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt




#read csv file
df = pd.read_csv("Email Analysis Dataset.csv")
df.columns



def main():
    st.markdown("## Univariate Statistics")

    # Create a container with a fixed width
    container = st.container()
    with container:
        # Set the width of the container
        st.markdown(f"""<style>.stcontainer{{width: 800px;}}</style>""", unsafe_allow_html=True)
        
        # Create columns inside the container
        #col1 = st.container()
        #col2 = st.container()
        col1, col1 = st.columns(2)
        
        
        with col1:
            st.markdown("## Sender Seniority")
            # Count the occurrences of each category
            category_counts = df['From seniority'].value_counts().reset_index()
            category_counts.columns = ['Seniority', 'Count']
            st.bar_chart(pd.DataFrame(category_counts), x = 'Seniority', y = 'Count')
            
         
        with col2:
            st.header("Sender Department")
            # Count the occurrences of each category
            dept_counts = df['From Department'].value_counts().reset_index()
            dept_counts.columns = ['Department', 'Count']
            
            st.bar_chart(pd.DataFrame(dept_counts), x = 'Department', y = 'Count')
            
        

        
      
    
    

    st.markdown('## Data Overview ')
    st.write(df)