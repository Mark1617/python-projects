import yfinance as yf
import streamlit as st
import pandas as pf

st.write("""
# Simple Stock Price Application

The closing prices and volume of Google are shown below.

""")

tickerSymbol = 'GOOGL'

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period='1d', start='2010-8-20', end='2020-8-20')

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)