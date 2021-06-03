import yfinance as yf
import streamlit as st

st.write("""
# Simple Stock Price App
### Shown are the stock **closing price** and **volume** of _**TESLA !**_ ###
#""")

tickerSymbol = 'TSLA'
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')
# Open High   Low    Close  Volume Dividends  Stock Splits
print(tickerData.quarterly_earnings)

st.line_chart(tickerDf.Close)
st.bar_chart(tickerDf.Volume)
st.area_chart(tickerDf.High)

