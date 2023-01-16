## This is mainly a test for new functions 

import streamlit as st
import pandas as pd
import base64
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import requests
import json 
import time

from streamlit.elements.selectbox import SelectboxMixin

# Makes page adapt to width changes
st.set_page_config(layout='wide')

st.title('Crypto Prices')
st.markdown("""
    This app fetches the prices of the top 100 cryptocurrencies.
""")

# New fn expander - Creates dropdown option
expander = st.expander('About')
expander.markdown("""
* **Python libraries:** base64, pandas, streamlit, numpy, matplotlib, seaborn, BeautifulSoup, requests, json, time
* **Data source:** [CoinMarketCap](http://coinmarketcap.com).
""")

# ----- Page Layout ----- #
column1 = st.sidebar
# New fn beta columns - Creates secondary columns (ratios determined in params)
column2, column3 = st.beta_columns((2,1))

# ----- Data Scraping ----- #
@st.cache
def load_data():
    cmc = requests.get('https://coinmarketcap.com')
    soup = BeautifulSoup(cmc.content, 'html.parser')
    # Turning HTML into a json and loading it
    data = soup.find('script', id='__NEXT_DATA__', type='application/json')
    print(data)
    coins = {}
    coin_data = json.loads(data.contents[0])
    listings = coin_data['props']['initialState']['cryptocurrency']['listingLatest']['data']
    for i in listings:
      coins[str(i['id'])] = i['slug']

    coin_name = []
    coin_symbol = []
    market_cap = []
    percent_change_1h = []
    percent_change_1d = []
    percent_change_7d = []
    price = []
    volume_24h = []

    # Need to separate all json keys we need into lists for assimilation into data frame
    for i in listings:
        coin_name.append(i['slug'])
        coin_symbol.append(i['symbol'])
        price.append(i['quote'][currency_unit_selector]['price'])
        percent_change_1h.append(i['quote'][currency_unit_selector]['percentChange1h'])
        percent_change_1d.append(i['quote'][currency_unit_selector]['percentChange24h'])
        percent_change_7d.append(i['quote'][currency_unit_selector]['percentChange7d'])
        market_cap.append(i['quote'][currency_unit_selector]['marketCap'])
        volume_24h.append(i['quote'][currency_unit_selector]['volume24h'])

    # Create data frame
    df = pd.DataFrame(columns=['coin_name', 'coin_symbol', 'market_cap', 'percent_change_1h', 'percent_change_24h', 'percent_change_7d', 'price', 'volume_24h'])
    df['coin_name'] = coin_name
    df['coin_symbol'] = coin_symbol
    df['price'] = price
    df['percent_change_1h'] = percent_change_1h
    df['percent_change_1d'] = percent_change_1d
    df['percent_change_7d'] = percent_change_7d
    df['market_cap'] = market_cap
    df['volume_24h'] = volume_24h
    return df

# ------ Column 1 Formatting ------ #
# - Titles - #
column1.header('Input Options')
currency_unit_selector = column1.selectbox('Select Currency', ('USD', 'BTC', 'ETH'))

data_frame = load_data()

# - Create Crypto Select - #
sorted_coin = sorted( data_frame['coin_symbol'])
selected_coin = column1.multiselect('Cryptocurrency', sorted_coin, sorted_coin)

data_frame_selected_coin = data_frame(data_frame['coin_symbol'].isin(selected_coin))

# - Coins on Display Slider - #
num_coins = column1.slider('Select the amount of coins to display:', 1, 100, 100)
data_frame_coins = data_frame_selected_coin[:num_coins]

# - Percent Change Time Periods - #
percent_period = column1.selectbox('Percentage change over time period', ['7 days', '1 day', '1 hour'])
percent_dict = {'7d':'percent_change_7d', '1 day':'percent_change_1d', '1 hour':'percent_change_1h'}
selected_period = percent_dict[percent_period]

# - Sorting Option - #
sort = column1.selectbox('Sort Values?', ['Yes', 'No'])

# ------ Column 2 Formatting ------ #
# - Titles - #
column2.subheader('Price Data of Selected Cryptocurrency')
column2.write(f'Data Dimension: {str(data_frame_selected_coin.shape[0])} and {str(data_frame_selected_coin.shape[1])} columns')

# - Data - #
column2.dataframe(data_frame_coins)

# - CSV Download Option - #
def csv_download():
    csv = data_frame.to_csv(index=False)
    # New functions encode() decode() - turns strings to and from bytes
    b64 = base64.b64encode(csv.encode()).decode()
    # HTML formatted download option
    href = f'<a href="data:file/csv;base64,{b64}" download="crypto.csv">Download CSV File</a>'

column2.markdown(csv_download(data_frame_selected_coin), unsafe_allow_html=True)

column2.subheader('Percentage Price Change')
change = pd.concat([data_frame_coins.coin_symbol, data_frame_coins.percent_change_1h, data_frame_coins.percent_change_1d, data_frame_coins.percent_change_7d], axis=1)
change = change.set_index('coin_symbol')
# If percentage change is positive in selected time period, it will be assigned value of one.
change['positive_percent_change_1h'] = change['percent_change_1h'] > 0
change['positive_percent_change_1d'] = change['percent_change_1d'] > 0
change['positive_percent_change_7d'] = change['percent_change_7d'] > 0
column2.dataframe(change)

# ------ Column 3 Formatting ------ #
# - Titles - #
column3.subheader('Bar plot - % Price Change')

# - Bar Plot - #
if percent_period == '7d':
    if sort == 'Yes':
                # Links data to sorting option in column 1
        data_change = change.sort_values(by=['percent_change_7d'])
    column3.write('*7 days period*')
    plt.figure(figsize=(5,25))
    plt.subplots_adjust(top = 1, bottom = 0)
        # Make positive percentage changes green, negative red.
    data_change['percent_change_7d'].plot(kind='barh', color=data_change.positive_percent_change_7d.map({True: 'g', False: 'r'}))
    column3.pyplot(plt)
elif percent_period == '1d':
    if sort == 'Yes':
        data_change = change.sort_values(by=['percent_change_1d'])
    column3.write('*1 day period*')
    plt.figure(figsize=(5,25))
    plt.subplots_adjust(top = 1, bottom = 0)
    data_change['percent_change_1d'].plot(kind='barh', color=data_change.positive_percent_change_1d.map({True: 'g', False: 'r'}))
    column3.pyplot(plt)
else:
    if sort == 'Yes':
        data_change = change.sort_values(by=['percent_change_1h'])
    column3.write('*1 hour period*')
    plt.figure(figsize=(5,25))
    plt.subplots_adjust(top = 1, bottom = 0)
    data_change['percent_change_1h'].plot(kind='barh', color=data_change.positive_percent_change_1h.map({True: 'g', False: 'r'}))
    column3.pyplot(plt)



