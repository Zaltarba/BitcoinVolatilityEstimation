import requests
import pandas as pd
from datetime import datetime, timedelta
import time

def fetch_candlestick_data(symbol, interval, start_date, end_date, limit=1000, hdf5_file='data/crypto_database.h5', key='candlestick_data'):
    url = "https://api.binance.com/api/v3/klines"
    
    # Convert dates to timestamps in milliseconds
    start_ts = int(datetime.strptime(start_date, '%Y-%m-%d %H:%M:%S').timestamp() * 1000)
    end_ts = int(datetime.strptime(end_date, '%Y-%m-%d %H:%M:%S').timestamp() * 1000)

    # Calculate the total number of steps
    total_steps = (end_ts - start_ts) // (limit * 60 * 1000) + 1

    # Initialize step counter
    step_counter = 0
    
    while start_ts < end_ts:
        params = {
            'symbol': symbol,
            'interval': interval,
            'startTime': start_ts,
            'endTime': min(start_ts + limit * 60 * 1000, end_ts),
            'limit': limit
        }
        
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            if not data:
                break
            df = pd.DataFrame(data, columns=[
                'Open_Time', 
                'Open', 
                'High', 
                'Low', 
                'Close', 
                'Volume', 
                'Close_Time', 
                'Quote_Asset_Volume', 
                'Number_of_Trades', 
                'Taker_Buy_Base_Asset_Volume', 
                'Taker_Buy_Quote_Asset_Volume', 
                'Ignore'
            ])
            
            # Convert timestamps to datetime
            df['Open_Time'] = pd.to_datetime(df['Open_Time'], unit='ms')
            del df['Close_Time']
            # Convert numeric columns to appropriate types
            df['Open'] = pd.to_numeric(df['Open'])
            df['High'] = pd.to_numeric(df['High'])
            df['Low'] = pd.to_numeric(df['Low'])
            df['Close'] = pd.to_numeric(df['Close'])
            df['Volume'] = pd.to_numeric(df['Volume'])
            df['Quote_Asset_Volume'] = pd.to_numeric(df['Quote_Asset_Volume'])
            df['Taker_Buy_Base_Asset_Volume'] = pd.to_numeric(df['Taker_Buy_Base_Asset_Volume'])
            df['Taker_Buy_Quote_Asset_Volume'] = pd.to_numeric(df['Taker_Buy_Quote_Asset_Volume'])

            # Set 'Open Time' as index
            df.set_index('Open_Time', inplace=True)

            # Store DataFrame in HDF5 file with min_itemsize to avoid column size issues
            df.to_hdf(
                hdf5_file, 
                key=key, 
                mode='a', 
                format='table', 
                append=True, 
                data_columns=True,
            )
            
            # Update step counter
            step_counter += 1
            
            # Print progress
            print(f"Step {step_counter}/{total_steps} completed.")
            
            start_ts = data[-1][0] + 1  # Move to the next timestamp
        else:
            print(f"Error: {response.status_code}")
            time.sleep(60)  # Wait a minute before retrying
            continue
        
        time.sleep(0.1)  # To avoid hitting rate limits

def main(symbol)->None:

    interval = '1m'  # 1-minute granularity
    start_date = '2018-08-17 00:00:00'
    end_date = '2024-08-17 00:00:00'
    
    # Fetch the data and store it in HDF5
    fetch_candlestick_data(
        symbol, 
        interval, 
        start_date, end_date, 
        hdf5_file='data/crypto_database.h5',
        key=symbol
        )

if __name__ == "__main__":
    symbol = 'BTCUSDT'
    main(symbol)
    symbol = 'ETHBTC'
    main(symbol)
    symbol = 'ETHUSDT'
    main(symbol)