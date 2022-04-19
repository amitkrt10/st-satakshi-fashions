# streamlit_app.py

import streamlit as st
from google.oauth2 import service_account
from gsheetsdb import connect
import pandas as pd
from plotly import graph_objs as go

st.title("**Satakshi Fashions**")
         
# Create a connection object.
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"],
    scopes=[
        "https://www.googleapis.com/auth/spreadsheets",
    ],
)
conn = connect(credentials=credentials)

# Perform SQL query on the Google Sheet.
# Uses st.cache to only rerun when the query changes or after 10 min.
@st.cache(ttl=600)
def run_query(query):
    rows = conn.execute(query, headers=1)
    rows = rows.fetchall()
    return rows

sheet_url = st.secrets["private_gsheets_url"]
rows = run_query(f'SELECT * FROM "{sheet_url}"')

data = pd.DataFrame(rows)

# Plot raw data
def plot_raw_data():
	fig = go.Figure()
	fig.add_trace(go.Scatter(x=data['Type'], y=data['SP'], name="Selling Price"))
	fig.add_trace(go.Scatter(x=data['Type'], y=data['CP'], name="Cost Price"))
	fig.layout.update(title_text='SP and CP Trend', xaxis_rangeslider_visible=True)
	st.plotly_chart(fig)
	
plot_raw_data()

st.write(df)
