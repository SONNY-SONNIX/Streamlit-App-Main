## Packages imported
import pandas as pd
#import numpy as np
import streamlit as st 
from PIL import Image

# Utils 

# Setup & config


# App 

# Set page title and layout
st.set_page_config(page_title='Time Series Prediction', layout='wide')

# Title and description
st.title('Time Series Prediction')
st.write('This app demonstrates a simple time series prediction model using ARIMA.')
#Image loader 
# Load and display background image
background_image = Image.open('C:/Users/otchi/Downloads/aron-visuals-BXOXnQ26B7o-unsplash.jpg')
st.image(background_image, use_column_width=True)
#st.image('C:/Users/otchi/Downloads/aron-visuals-BXOXnQ26B7o-unsplash.jpg')
## Form 
# Upload CSV file
uploaded_file = st.file_uploader('Upload a CSV file', type=['csv'])

# Load and display data
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.subheader('Data')
    st.write(data)

 
    # Select column for time series
    column = st.selectbox('Select the time series column', data.columns)
    # Create date selection dropdown
selected_date = st.selectbox('Select a Date', data['date'])

# Filter data for selected date
selected_data = data[data['date'] == selected_date]

# Display selected date and corresponding sales
if not selected_data.empty:
    st.subheader('Selected Date: ' + selected_date)
    st.write('sales: ' + str(selected_data['sales'].values[0]))


    # Model parameters
    order = st.text_input('Enter the order for ARIMA (p, d, q)', '1, 0, 1')
   # Train the ARIMA model
    try:
        p, d, q = map(int, order.split(','))
        model = ARIMA(data[column], order=(p, d, q))
        model_fit = model.fit()

        # Forecasting
        forecast_steps = st.number_input('Enter the number of steps for forecasting', min_value=1, value=10)
        forecast = model_fit.forecast(steps=forecast_steps)

        # Display forecasted values
        st.subheader('Forecasted Values')
        st.write(forecast)
    except:
        st.error('Error: Invalid ARIMA order. Please enter valid order values.')
 
with st.form("my_form") as form:
    name = st.text_input(label="Enter your name ,please ....")
    p = st.number_input("Enter your autoregressive order (p),please ....")
    d = st.number_input("Enter your ,integrated order(d),please ....")
    q = st.number_input("Enter your moving average order(q),please ....")
    submit = st.form_submit_button()




    # Add footer
st.sidebar.markdown('Created by [Seville]')

#print ("[Info] Here is my name : {name}")

 