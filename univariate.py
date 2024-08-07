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
        col1 = st.container()
        col2 = st.container()
        col5, col6 = st.columns([6,4])
        
        
        with col1:
            st.markdown("## Sender Seniority")
            # Count the occurrences of each category
            category_counts = df['From seniority'].value_counts().reset_index()
            category_counts.columns = ['Seniority', 'Count']

            # Display the bar chart using Streamlit
            fig, ax = plt.subplots()
            bars = ax.bar(category_counts['Seniority'], category_counts['Count'])
            max_value = max(category_counts['Count'])
            max_index = category_counts['Count'].idxmax()
            bars[max_index].set_color('red')  # Set the longest bar to red
            for i, v in enumerate(category_counts['Count']):
                ax.text(i, v + 1, str(v), color='black', ha='center')
                
            st.pyplot(fig)
         
        with col2:
            st.markdown("## Sender Department")
            # Count the occurrences of each category
            dept_counts = df['From Department'].value_counts().reset_index()
            dept_counts.columns = ['Department', 'Count']

            # Display the bar chart using Streamlit
            fig, ax = plt.subplots()
            bars = ax.barh(dept_counts['Department'], dept_counts['Count'])
            max_value = max(dept_counts['Count'])
            max_index = dept_counts['Count'].idxmax()
            bars[max_index].set_color('green')  # Set the longest bar to red
            for i, v in enumerate(dept_counts['Count']):
                ax.text(i, v + 1, str(v), color='black', ha='center')
                
            st.pyplot(fig)
        with col3:
            st.markdown("## Variable 3")

        
        with col4:
            st.markdown("## Variable 4")
        with col5:
            st.markdown("## Variable 5")
        with col6:
            st.markdown("## Variable 6")

        
      
    
    

    st.markdown('## Data Overview ')
    st.write(df)