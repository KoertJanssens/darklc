import streamlit as st
import pandas as pd
import mysql.connector

# MySQL connection details
db_config = {
    'host': st.secrets["mysql"]["host"],
    'user': st.secrets["mysql"]["user"],
    'password': st.secrets["mysql"]["password"],
    'database': st.secrets["mysql"]["database"]
}

# Connect to MySQL
conn = mysql.connector.connect(**db_config)

# Query the database
query = "select charactername, characterclass, characterposition from dkplist order by characterposition asc"
df = pd.read_sql(query, conn)

# Close connection
conn.close()

# Display in Streamlit
st.title("MySQL Data in Streamlit")

st.subheader("Static Table")
st.table(df)

st.subheader("Interactive Table")
st.dataframe(df)
