#import yfinance as yf
import streamlit as st
import altair as alt
from PIL import Image
# this is great
# this is best as well
# this is 2nd commit


st.write("""
# Simple Stock Price App
Shown are the stock closing price and volume of tickerSymbol1 and tickerSymbol2!
""")

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#define the ticker symbol
tickerSymbol1 = 'DOGE-USD'
#tickerSymbol2 = 'LUV'
#get data on this ticker
#tickerData1 = yf.Ticker(tickerSymbol1)
#tickerData2 = yf.Ticker(tickerSymbol2)

#get the calendar

#tickerData1.calendar
#tickerData2.calendar
# this is great
# recommendation
#tickerData1.recommendations
#get the historical prices for this ticker
#tickerDf1 = tickerData1.history(period='1d', start='2010-5-31', end='2020-5-31')
#tickerDf2 = tickerData2.history(period='1d', start='2010-5-31', end='2020-5-31')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.write("""
## closing price and volume of Doge
""")
#st.line_chart(tickerDf1.Close)
#st.line_chart(tickerDf1.Volume)

#st.write("""
### closing price and volume of Southwest
#""")
#st.line_chart(tickerDf2.Close)
#st.line_chart(tickerDf2.Volume)