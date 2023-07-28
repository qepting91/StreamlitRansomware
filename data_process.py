import pandas as pd

def process_data(data):
    data['Date'] = pd.to_datetime(data['Date']).dt.date
    return data