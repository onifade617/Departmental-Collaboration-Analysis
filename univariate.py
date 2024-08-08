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
        col1, col2 = st.columns(2)
        col3, col4 = st.columns(2)
        col5, col6 = st.columns(2)
        col7, col8 = st.columns(2)
        col9, col10 = st.columns(2)
        col11, col12 = st.columns(2)
         
        
        with col3:
            st.header("Sender Name")
            # Count the occurrences of each category
            Sname_counts = df['From Name'].value_counts().reset_index()
            Sname_counts.columns = ['Name', 'Count']
            
            st.bar_chart(pd.DataFrame(Sname_counts), x = 'Name', y = 'Count')
        
        with col1:
            st.markdown("## Sender Seniority")
            # Count the occurrences of each category
            category_counts = df['From seniority'].value_counts().reset_index()
            category_counts.columns = ['Seniority', 'Count']
            st.bar_chart(pd.DataFrame(category_counts), x = 'Seniority',  y = 'Count')
            
         
        with col2:
            st.header("Sender Department")
            # Count the occurrences of each category
            dept_counts = df['From Department'].value_counts().reset_index()
            dept_counts.columns = ['Department', 'Count']
            
            st.bar_chart(pd.DataFrame(dept_counts), x = 'Department', y = 'Count')
            
            
        
            
        with col4:
            st.header("Receiver Name")
            # Count the occurrences of each category
            Rname_counts = df['To Name'].value_counts().reset_index()
            Rname_counts.columns = ['Name', 'Count']
            
            st.bar_chart(pd.DataFrame(Rname_counts), x = 'Name', y = 'Count')
            
        with col5:
            st.header("Receiver Seniority")
            # Count the occurrences of each category
            Rcategory_counts = df['To seniority'].value_counts().reset_index()
            Rcategory_counts.columns = ['Seniority', 'Count']
            
            st.bar_chart(pd.DataFrame(Rcategory_counts), x = 'Seniority', y = 'Count')
            
        with col6:
             st.header("Receiver Department")
             # Count the occurrences of each category
             rdept_counts = df['To Department'].value_counts().reset_index()
             rdept_counts.columns = ['Department', 'Count']
             
             st.bar_chart(pd.DataFrame(rdept_counts), x = 'Department', y = 'Count')
             
             
        with col7:
             st.header("Email Topic")
             # Count the occurrences of each category
             topic_counts = df['Email topic'].value_counts().reset_index()
             topic_counts.columns = ['Topics', 'Count']
             
             st.bar_chart(pd.DataFrame(topic_counts), x = 'Topics', y = 'Count')
             
             
        with col8:
             st.header("Sentiment")
             # Count the occurrences of each category
             senti_counts = df['Sentiment'].value_counts().reset_index()
             senti_counts.columns = ['Sentiment', 'Count']
             
             st.bar_chart(pd.DataFrame(senti_counts), x = 'Sentiment', y = 'Count')
             
        with col9:
             st.header("Opened File")
             # Count the occurrences of each category
             file_counts = df['Is opened?'].value_counts().reset_index()
             file_counts.columns = ['File', 'Count']
             
             st.bar_chart(pd.DataFrame(file_counts), x = 'File', y = 'Count')
             
             
        with col10:
             st.header("Device Used")
             # Count the occurrences of each category
             device_counts = df['Device'].value_counts().reset_index()
             device_counts.columns = ['Device', 'Count']
             
             st.bar_chart(pd.DataFrame(device_counts), x = 'Device', y = 'Count')
        
        with col11:
             st.header("File sent Within work hours")
             # Count the occurrences of each category
             hour_counts = df['Within work hours'].value_counts().reset_index()
             hour_counts.columns = ['Opened within work hour', 'Count']
             
             st.bar_chart(pd.DataFrame(hour_counts), x = 'Opened within work hour', y = 'Count')
             
             
        with col12:
             st.header("File sent Within work hours")
             # Count the occurrences of each category
             hour_counts = df['Within workdays'].value_counts().reset_index()
             hour_counts.columns = ['Opened within work hour', 'Count']
             
             st.bar_chart(pd.DataFrame(hour_counts), x = 'Opened within work hour', y = 'Count')
        

        
      
    
    

    st.markdown('## Data Overview ')
    st.write(df)