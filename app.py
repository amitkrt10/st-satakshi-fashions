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

@st.cache(ttl=600)
def read_gsheet(sheetId,sheetName):
	url = f"https://docs.google.com/spreadsheets/d/{sheetId}/gviz/tq?tqx=out:csv&sheet={sheetName}"
	data = pd.read_csv(urllib.request.urlopen(url))
	return data

salesDf = read_gsheet("1kYeoUISggtO79cZnr0zyJbnGDPFVj6HFE_1Sgti9NZg","SalesCopy")
purchaseDf = read_gsheet("1kYeoUISggtO79cZnr0zyJbnGDPFVj6HFE_1Sgti9NZg","PurchaseCopy")

typeList = list(purchaseDf['Type'].unique())
typeList.sort()
col1, col2 = st.columns(2)
col1.subheader("**Price List**")
selectCategory = col1.selectbox("Select Category",typeList)
productList = list(purchaseDf[purchaseDf['Type']==selectCategory]['Product Name'])
productList.sort()
selectProduct = col1.selectbox("Select Product",productList)

st.write(selectProduct)
price = int(purchaseDf[(purchaseDf['Type']==selectCategory) & (purchaseDf['Product Name']==selectProduct)]['Unit CP With GST + Transport'])
col1.info("Unit Price = ₹ "+str(price*2))
c1,c2,c3,c4 = st.columns(4)
c1.write("fid = "+str(int(price*1.4)))
c2.write("oid = "+str(int(price*1)))
