from pandas.core.indexes import interval
import streamlit as st
import pandas as pd
import base64
import matplotlib.pyplot as plt
import yfinance as yf

st.title(' S&P 500 ')

st.markdown("""
This app retrieves the list of the **S&P 500** (from Wikipedia) and its corresponding **stock closing price** (year-to-date)!
* **Python libraries:** base64, pandas, streamlit, numpy, matplotlib, yfinance
* **Data source:** [Wikipedia](https://en.wikipedia.org/wiki/List_of_S%26P_500_companies)
""")

st.sidebar.header('User Input Features')

# Scrape the data

@st.cache   # Store loaded data to cache to drop runtime
def load_data():
    url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
    html = pd.read_html(url, header=0)
    df = html[0]
    return df

data_frame = load_data()
sector = data_frame.groupby('GICS Sector')

# Sidebar
sorted_sector_unique = sorted(data_frame['GICS Sector'].unique())
selected_sector = st.sidebar.multiselect('Sector', sorted_sector_unique, sorted_sector_unique)

# Filtering Data
df_selected_sector = data_frame[(data_frame['GICS Sector'].isin(selected_sector))]

st.header('Display Companies in Selected Sector')
st.write(f'Data Dimension {str(df_selected_sector.shape[0])} rows and {df_selected_sector.shape[1]} columns.')
st.dataframe(df_selected_sector)

# Make data downloadable
def file_download():
    csv =  data_frame.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="SP500.csv">Download CSV File</a>'
    return href

st.markdown(file_download(df_selected_sector), unsafe_allow_html=True)

# Only displaying 10 companies but can choose as many as desired.
data = yf.download(
    tickers = list(df_selected_sector[:10].Symbol),
    interval = '1d',
    period = 'ytd',
    group_by = 'ticker',
    auto_adjust = True,
    prepost = True,
    threads = True,
    proxy = None 
)

# Make the Plot 
def price_plot(symbol):
    df = pd.DataFrame(data[symbol].Close)
    df['Date'] = df.index
    plt.fill_between(df.Date, df.Close, color='skyblue', alpha=0.3)
    plt.plot(df.Date, df.Close, color='skyblue', alpha=0.8)
    plt.xticks(rotation=90)
    plt.title(symbol, fontweight='bold')
    return st.pyplot()

# Note number of companies need to be lower than displayed.
num_company = st.sidebar.slider('Number of Companies', 1, 10)
if st.button('Show Plots'):
    st.header('Stock Closing Price')
    for i in list(df_selected_sector.Symbol)[:num_company]:
        price_plot(i)