# File is Prophet dependent, which also might make it pretty annoying
import Prophet
import dateutil
from datetime import datetime, timedelta

def predict_future(testDf, timestamp = "date_time"):
    # Takes in trained model and predicts the future
    # find number of hours to predict: ceil of hours in testDf
    df['ts'] = df[timestamp]
    timeDelta = max(testDf['ts']) -min(testDf['ts'])
    hours = int(timeDelta.days*24 + timeDelta.seconds/(60*60))+1
    future = m.make_future_dataframe(periods = hours, freq = 'H')
    forecast = m.predict(future)
    return forecast
