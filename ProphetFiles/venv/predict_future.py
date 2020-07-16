# File is Prophet dependent, which also might make it pretty annoying
import Prophet
import math as mt
import dateutil
from datetime import datetime, timedelta


# Takes in a test DataFrame and the time stamp column and returns a prediction
def predict_future(testDf, timestamp="date_time"):
    # Takes in trained model and predicts the future
    # find number of hours to predict: ceil of hours in testDf
    testDf = testDf.assign(ts=testDf.get(timestamp))

    # If a column is string, convert to date/time
    if (testDf.applymap(type).eq(str).any()['ts']):
        testDf['ts'] = pd.to_datetime(testDf['ts'])
    try:
        timeDelta = max(testDf['ts']) - min(testDf['ts'])
    except TypeError:
        print("Please ensure that you've properly entered your timestamp column")
    hours = int(timeDelta.days * 24 + timeDelta.seconds / (60 * 60)) + 1
    future = m.make_future_dataframe(periods=hours, freq='H')
    forecast = m.predict(future)
    return forecast

