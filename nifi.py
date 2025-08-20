import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

# Page config
st.set_page_config(page_title="📈 Nifty Stocks Explorer", layout="wide")

# Load Data
@st.cache_data
def load_data():
    df = pd.read_csv("Nifty_Stocks.csv")
    df["Date"] = pd.to_datetime(df["Date"])
    return df

df = load_data()

# Title
st.title("📊 Nifty Stocks Interactive Explorer")

# Category selection
categories = df["Category"].unique()
category = st.selectbox("Select Category", categories)

# Filter by category
df_cat = df[df["Category"] == category]

# Symbol selection
symbols = df_cat["Symbol"].unique()
symbol = st.selectbox("Select Symbol", symbols)

# Filter by symbol
df_symbol = df_cat[df_cat["Symbol"] == symbol]

# Plotting
fig, ax = plt.subplots(figsize=(10, 5))
sb.lineplot(x="Date", y="Close", data=df_symbol, ax=ax)
ax.set_title(f"{symbol} Closing Price Trend", fontsize=14)
ax.set_xlabel("Date")
ax.set_ylabel("Closing Price")
plt.xticks(rotation=90)

st.pyplot(fig)
