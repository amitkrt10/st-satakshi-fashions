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
# SSL Verification
ssl._create_default_https_context = ssl._create_unverified_context
# Logo
st.image("satakshi-fashions-logo.png", use_column_width=True)
# Read Data Function
@st.cache(ttl=600)
def read_gsheet(sheetId,sheetName):
	url = f"https://docs.google.com/spreadsheets/d/{sheetId}/gviz/tq?tqx=out:csv&sheet={sheetName}"
	data = pd.read_csv(urllib.request.urlopen(url))
	return data

salesDf = read_gsheet("1kYeoUISggtO79cZnr0zyJbnGDPFVj6HFE_1Sgti9NZg","SalesCopy")
purchaseDf = read_gsheet("1kYeoUISggtO79cZnr0zyJbnGDPFVj6HFE_1Sgti9NZg","PurchaseCopy")

st.markdown("<h3 style='text-align: center;'>Price List</h3>", unsafe_allow_html=True)
typeList = list(purchaseDf['Type'].unique())
typeList.sort()
selectCategory = st.selectbox("Select Category",typeList)
productList = list(purchaseDf[purchaseDf['Type']==selectCategory]['Product Name'])
productList.sort()
selectProduct = st.selectbox("Select Product",productList)
price = int(purchaseDf[(purchaseDf['Type']==selectCategory) & (purchaseDf['Product Name']==selectProduct)]['Unit CP With GST + Transport'])
st.info("# Unit Price = ₹ "+str(price*2))
st.write("fid : "+str(int(price*1.4)))
st.write("oid : "+str(int(price*1)))

st.markdown("<h3 style='text-align: center;'>Analytics</h3>", unsafe_allow_html=True)

uniqueCustomers = len(salesDf['Mobile'].unique())
st.success("### Total Customers = "+str(uniqueCustomers))

sp = salesDf['Total Selling Price'].sum()
st.warning("### Total Revenue = ₹ "+str(int(sp)))

cp = salesDf['Total Cost Price'].sum()
st.warning("### Total Sales Cost = ₹ "+str(int(cp)))

salesProfit = int((sp-cp)/cp*100)
if salesProfit>0:
	st.success("### Sales Profit = "+str(salesProfit)+"%")
else:
	st.error("### Sales Profit = "+str(salesProfit)+"%")

tcp = purchaseDf['Total CP'].sum()
st.warning("### Total Investment = ₹ "+str(int(tcp)))

netProfit = int((sp-tcp)/tcp*100)
if netProfit>0:
	st.success("### Net Profit = "+str(netProfit)+"%")
else:
	st.error("### Net Profit = "+str(netProfit)+"%")