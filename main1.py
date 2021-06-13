import yfinance as yf
import streamlit as st
import pandas as pd


st.write("""
# Simple Stock Price app

Shown are the stock price and volume of google!!!!!

""")

symbol = 'GOOGL'  #ticker symbol of google

tickerdata =  yf.Ticker(symbol)

df = tickerdata.history(period='1d', start='2010-5-31',end='2020-5-31')

st.write("""
# Closing price!!
""")
st.line_chart(df.Close)
st.write("""
# Volume price!!
""")
st.line_chart(df.Volume)