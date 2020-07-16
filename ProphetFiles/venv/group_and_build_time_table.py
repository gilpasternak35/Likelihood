import pandas as pds
import dateutil
from datetime import datetime, timedelta


def group_and_build_time_table(truncated_data):
    try:
        grouped_counts = truncated_data.value_counts()

    # In the case that the user enters a list
    except AttributeError:
        print("Please enter a valid DataFrame whose Date/Time columns has been preprocessed with truncate_training_set")

    # In the case that the user enters a series
    except TypeError:
        print("Please enter a valid DataFrame whose Date/Time columns has been preprocessed with truncate_training_set")


    # Redefining values for sake of Prophet regression-like procedures
    prophet_df = pd.DataFrame({'ds' : grouped_counts.index,'y' : np.log10(grouped_counts.values)})
    return prophet_df
