import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader as data
from keras.models import load_model
import streamlit as st


import yfinance as yf

st.title('Stock Trend Prediction')

user_input = st.text_input('Enter Sock Ticker')

# Define the ticker symbol
tickerSymbol = user_input

# Get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

# Get historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-01-01', end='2019-12-31')

st.subheader('Data from 2010-2019')
st.write(tickerDf.describe())