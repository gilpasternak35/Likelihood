import pandas as pds
import dateutil
from datetime import datetime, timedelta


def group_and_build_time_table(truncated_data):
    grouped_counts = truncated_data.value_counts()
    prophet_df = pd.DataFrame({'ds':grouped_counts.index,'y':np.log10(grouped_counts.values)})
    return prophet_df
