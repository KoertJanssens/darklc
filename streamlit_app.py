import streamlit as st
import pandas as pd
import mysql.connector

st.title("Dark Alignment Loot Council Dashboard")

try:
    st.write("🔄 Connecting to MySQL database...")
    
    db_config = {
        'host': st.secrets["mysql"]["host"],
        'port': st.secrets["mysql"]["port"],
        'user': st.secrets["mysql"]["user"],
        'password': st.secrets["mysql"]["password"],
        'database': st.secrets["mysql"]["database"]
    }

    st.write(db_config['host'])
    st.write(db_config['port'])

    import requests
    ip = requests.get('https://api.ipify.org').text
    st.write(f"My public IP is {ip}")

    # Connect to MySQL
    conn = mysql.connector.connect(**db_config)
    st.write("✅ Successfully connected!")

    # Query the database
    query = "SELECT charactername, characterclass, characterposition FROM dkplist ORDER BY characterposition ASC"
    st.write(f"📥 Running query: {query}")
    df = pd.read_sql(query, conn)
    st.write(f"📊 Retrieved {len(df)} rows.")

except mysql.connector.Error as err:
    st.error(f"❌ MySQL Error: {err}")
    df = pd.DataFrame()  # empty dataframe to avoid errors

finally:
    if 'conn' in locals() and conn.is_connected():
        conn.close()
        st.write("🔒 Database connection closed.")

if not df.empty:
    st.subheader("Static Table")
    st.table(df)

    st.subheader("Interactive Table")
    st.dataframe(df)
else:
    st.warning("No data to display.")
