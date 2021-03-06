import Prophet
import dateutil
from datetime import datetime, timedelta
import pandas as pd


# Takes in a model that has been trained on country, plots graphs for visualization
def visualize(m):
    # plotting for debug only
    try:
        fig = m.plot(fcst)
        fig = m.plot_components(fcst)
    except error:
        print("This function requires a Prophet DataFrame")

    return fig

