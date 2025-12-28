import streamlit as st
import pickle
from sklearn.preprocessing import StandardScaler
import pandas as pd
import time
from sklearn.datasets import fetch_california_housing
st.title('🏠House Price prediction using ML')
st.image('https://www.colliers.com/en-in/news/press-release-housing-price-tracker-report-2022')

