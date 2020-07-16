import pandas as pd
import dateutil
from datetime import datetime, timedelta


def find_surprise(truncated_data, fcst, timestamp = "date_time"):
    truncated_data = truncated_data.assign(ts=testDf.get(timestamp))

    # If a column is string, convert to date/time
    if truncated_data.applymap(type).eq(str).any()['ts']:
        truncated_data['ts'] = pd.to_datetime(truncated_data['ts'])

    try:
        grouped_counts = truncated_data.value_counts()
    except AttributeError:
        print("Arguments should be a valid Pandas DataFrame and the name of your timestamp column")
        
    prophetTestDf = pd.DataFrame({'ds':grouped_counts.index,
                                  'y':np.log10(grouped_counts.values),
                                  'y_linear':grouped_counts.values})

    # find p-value
    prophet_results = []

    for ii in range(len(prophetTestDf)):
        ts = prophetTestDf['ds'][ii]
        fcstExample = fcst[fcst['ds'] == ts]
        mean = fcstExample['yhat'].iloc[0]
        stdev = (fcstExample['yhat_upper'].iloc[0] - fcstExample['yhat_lower'].iloc[0])/2
        p = scipy.stats.norm(mean, stdev).cdf(prophetTestDf['y'][ii])
        p = min(p,1-p)

        prophet_results.append({"column":"Forecast",
                           "category":str(ts),
                           "count":prophetTestDf['y_linear'][ii],
                           "p": p,
                           "estimated_count":int(np.round(np.power(10,mean))),
                           })

    prophetResultsDf = pd.DataFrame.from_records(prophet_results).sort_values('p')
    prophetResultsDf['surprise'] = -np.log2(prophetResultsDf['p'])
    return prophetResultsDf
