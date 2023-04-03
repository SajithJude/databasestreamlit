import streamlit as st
import pandas as pd
import pyodbc

# Establish a connection to the database
server = 'IP-0A7CE336'
database = 'bot4'
username = 'mediawide'
password = 'DB!@#Pock'

connection = pyodbc.connect('DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)

# Write a SQL query to retrieve data from the database
query = "SELECT * FROM YourTable"
df = pd.read_sql(query, connection)

# Display the data in a Streamlit app
st.dataframe(df)
