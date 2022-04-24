import streamlit as st
import pandas as pd
import numpy as np
import urllib
from urllib.request import urlopen
import ssl
import warnings
warnings.filterwarnings("ignore")

# Configure app display
st.set_page_config(page_title="Satakshi Fasion", layout="wide",initial_sidebar_state='collapsed')

ssl._create_default_https_context = ssl._create_unverified_context

st.image("satakshi-fashions-logo.png", use_column_width=True)

@st.cache(ttl=600)
def read_gsheet(sheetId,sheetName):
	url = f"https://docs.google.com/spreadsheets/d/{sheetId}/gviz/tq?tqx=out:csv&sheet={sheetName}"
	data = pd.read_csv(urllib.request.urlopen(url))
	return data

salesDf = read_gsheet("1kYeoUISggtO79cZnr0zyJbnGDPFVj6HFE_1Sgti9NZg","SalesCopy")
purchaseDf = read_gsheet("1kYeoUISggtO79cZnr0zyJbnGDPFVj6HFE_1Sgti9NZg","PurchaseCopy")

typeList = list(purchaseDf['Type'].unique())
typeList.sort()
st.markdown("<h3 style='text-align: center; color: Green;'>Today's Performance Dashboard</h3>", unsafe_allow_html=True)
#st.subheader("**Price List**")
selectCategory = st.selectbox("Select Category",typeList)
productList = list(purchaseDf[purchaseDf['Type']==selectCategory]['Product Name'])
productList.sort()
selectProduct = st.selectbox("Select Product",productList)
price = int(purchaseDf[(purchaseDf['Type']==selectCategory) & (purchaseDf['Product Name']==selectProduct)]['Unit CP With GST + Transport'])
st.info("Unit Price = ₹ "+str(price*2))
st.write("fid : "+str(int(price*1.4)))
st.write("oid : "+str(int(price*1)))
