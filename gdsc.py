import streamlit as st
import yfinance as yf

st.write("""
# Simple Stock Price App

Shown are the stock closing price and volume of Google!


""")
tickerSymbol = 'GOOG'

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period='1d',start='2010-6-28', end='2020-6-29')

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)
