
import streamlit as st
import datetime as dt
from PIL import Image

#....................................................#
#expand page to full width
st.set_page_config(layout="wide")
#....................................................#
st.title("Crypocurrency Analyzer")

st.write("This web app fetches the prices of cryptocurrencies and plots them on a graph") 

#....................................................#
#Side bar 
side = st.sidebar

side.header("Input Options")

crypto_ticker = side.text_input("Input cryptocurrency ticker")
currency_ticker = side.text_input("Input currency ticker")
year = side.text_input("Input year")
month = side.text_input("Input month")
day = side.text_input("Input day")

#....................................................#
