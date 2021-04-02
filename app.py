import pandas_datareader as pdr
import streamlit as st
import datetime as dt
from PIL import Image

#....................................................#
#expand page to full width
st.set_page_config(layout="wide")
#....................................................#

#....................................................#
#load and display image
image = Image.open("crypto_logo.jpg")
st.image(image, width = 250)

#set title 
st.title("Crypocurrency Trend Analyzer")
st.write("This web app fetches the prices of cryptocurrencies and plots them on a graph") 
#....................................................#

#....................................................#
#init sidebar 
side = st.sidebar

#add sidebar options
side.header("Input Details")
crypto_ticker = side.text_input("Input cryptocurrency ticker")
currency_ticker = side.text_input("Input currency ticker")
start_date = side.date_input("Select date to start analysis")
end_date = side.date_input("Select date to end analysis")

#function to get data
def fetch_data(ticker, currency, start_date, end_date):
    """function to fetch cryptocurrency data"""
    scraped_data = pdr.DataReader(f"{ticker}-{currency}","yahoo", start_date,end_date)
    return scraped_data

if side.button("fetch data"):
    scraped_data = fetch_data(crypto_ticker, currency_ticker, start_date, end_date)
    st.success("Data successfully scraped")

    #display needed data in dataframe
    data = scraped_data[['High','Low','Open','Close']]
    st.dataframe(data = data)

    #display data using graph
    st.line_chart(data, width=50, height=500)



