# File is Prophet dependent, which also might make it pretty annoying
import Prophet
import dateutil
from datetime import datetime, timedelta


# Takes in the the data set and the prophet data set returned by the ast option
def train_model_on_country(prophet_df, country="US"):
    # Train model
    m = Prophet(#daily_seasonality = True,
                #yearly_seasonality = False,
                #weekly_seasonality = True,
                #growth='linear',
                interval_width=0.68 # one sigma
               )
    m.add_country_holidays(country_name=country)

    m.fit(prophet_df)
    return m

